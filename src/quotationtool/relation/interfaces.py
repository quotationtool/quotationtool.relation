import zope.interface
import zope.schema
from zope.interface.common.interfaces import IException
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('quotationtool')


class IRelationPreconditionError(IException):
    """An exception concerning relation constraints check.
    A view is registered for this interface."""


class RelationPreconditionError(zope.schema._bootstrapinterfaces.ValidationError):
    __doc__ = _(u"Invalid relation! The precondition violated.")

    zope.interface.implements(IRelationPreconditionError)


class IRelation(zope.schema.interfaces.IField):
    """zope.schema.Object checks if the schema is provided. This field
    only checks it one of the interfaces in precondition is provided.

    See quotationtool.relation.schema.Relation for detials."""

    precondition = zope.schema.List(
        title = u"Precondition",
        description = u"At least one Interface of this list must be provided by an object, that the relation path points to.",
        value_type = zope.schema.InterfaceField(title = u"Interface"),
        default = [],
        )
