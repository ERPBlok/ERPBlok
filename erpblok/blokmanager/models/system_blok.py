from anyblok.blok import BlokManager
from erpblok.blok import Blok as ERPBlok
from anyblok.declarations import Declarations
from anyblok.column import Boolean, String, Color
from anyblok_pyramid.bloks.pyramid.restrict import restrict_query_by_user


@Declarations.register(Declarations.Model.System)
class Blok:

    come_from_erpblok = Boolean(default=False)
    category = String()
    color = Color()

    @classmethod
    def update_list(cls):
        super(Blok, cls).update_list()
        for order, blok_name in enumerate(BlokManager.ordered_bloks):
            b = cls.query().filter(cls.name == blok_name).one_or_none()
            blok = BlokManager.bloks[blok_name]
            values = {}

            if issubclass(blok, ERPBlok):
                values.update(come_from_erpblok=True, category=blok.category)
            else:
                values.update(come_from_erpblok=False, category=None)

            b.update(**values)

    @restrict_query_by_user()
    def see_only_blok_come_from_of_erpblok(cls, query, user):
        return query.filter_by(come_from_erpblok=True)

    def furetui_update(self, **kwargs):
        self.update(**kwargs)
