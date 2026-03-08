from anyblok import Declarations


register = Declarations.register
Mixin = Declarations.Mixin


@register(Mixin)
class MailMixin:

    def message_post(self, body, author=None):
        Message = self.anyblok.Model.Message
        Follower = self.anyblok.Model.Follower
        Notification = self.anyblok.Model.Notification

        message = Message.insert(
            res_model=self.__registry_name__,
            res_id=self.id,
            body=body,
            author=author
        )

        followers = Follower.query().filter(
            Follower.res_model == self.__registry_name__,
            Follower.res_id == self.id
        ).all()

        for follower in followers:
            if author and follower.partner == author:
                continue

            Notification.insert(
                message=message,
                partner=follower.partner
            )
        
        return message

    def message_subscribe(self, partner):
        Follower = self.anyblok.Model.Follower
        return Follower.insert(
            res_model=self.__registry_name__,
            res_id=self.id,
            partner=partner
        )
