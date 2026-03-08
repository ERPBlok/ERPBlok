from anyblok import Declarations


register = Declarations.register
Model = Declarations.Model


@register(Model.Security)
class Logic:
    """Class to hold security validation logic
    """

    @classmethod
    def check_access(cls, model_name, mode, user):
        """Check if a user has access to a model in a specific mode
        
        :param model_name: Name of the model (e.g., 'Model.Partner')
        :param mode: 'read', 'write', 'create', or 'unlink'
        :param user: The user object
        :return: Boolean
        """
        if user.is_admin:
            return True

        AccessRight = cls.anyblok.Model.Security.Access.Right
        
        # Collect all groups of the user
        group_ids = [group.id for group in user.groups]
        if not group_ids:
            return False

        # Query access rights for these groups and the model
        perm_field = f"perm_{mode}"
        
        # Check if any group has the permission
        has_access = AccessRight.query().filter(
            AccessRight.model_name == model_name,
            AccessRight.group_id.in_(group_ids),
            getattr(AccessRight, perm_field) == True
        ).count() > 0

        return has_access

    @classmethod
    def apply_rules(cls, query, user):
        """Apply record rules (AccessRule) to a query
        
        :param query: SQLAlchemy query
        :param user: The user object
        :return: Filtered query
        """
        if user.is_admin:
            return query

        model_name = query.anyblok.Model._anyblok_name
        AccessRule = cls.anyblok.Model.Security.Access.Rule
        
        group_ids = [group.id for group in user.groups]
        if not group_ids:
            return query # Or return a query that returns nothing?

        # Fetch rules for this model and user's groups
        rules = AccessRule.query().filter(
            AccessRule.model_name == model_name,
            AccessRule.group_id.in_(group_ids)
        ).all()

        if not rules:
            return query

        # Apply each rule's domain_force
        # For the sake of this example, we assume domain_force is an 
        # expression that can be evaluated or used in a filter.
        # In a real system, this would be a more complex parser.
        for rule in rules:
            # Placeholder for domain evaluation logic
            # e.g. query = query.filter(evaluate(rule.domain_force, query.anyblok.Model, user))
            pass
            
        return query
