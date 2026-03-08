from anyblok import Declarations


register = Declarations.register
Mixin = Declarations.Mixin


@register(Mixin)
class DocumentMixin:

    @property
    def attachments(self):
        Attachment = self.anyblok.Model.Attachment
        return Attachment.query().filter(
            Attachment.res_model == self.__registry_name__,
            Attachment.res_id == self.id
        ).all()
