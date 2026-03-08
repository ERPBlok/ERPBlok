from functools import wraps
from anyblok import Declarations


class AccessError(Exception):
    """Exception raised when access is denied
    """
    pass


def require_access(model_name, mode):
    """Decorator to check access before executing an API method
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # In a real API, the user would be retrieved from the session or token
            # For this example, we assume the user is passed in kwargs or available in context
            # This is a placeholder for the actual user retrieval logic
            user = kwargs.get('user')
            if not user:
                raise AccessError("No user identified for this request")

            Logic = Declarations.Model.Security.Logic
            if not Logic.check_access(model_name, mode, user):
                raise AccessError(f"Access denied for {model_name} in mode {mode}")

            result = func(*args, **kwargs)
            
            # If the result is a query, we automatically apply record rules
            if hasattr(result, 'filter') and hasattr(result, 'anyblok'):
                result = Logic.apply_rules(result, user)
                
            return result
        return wrapper
    return decorator
