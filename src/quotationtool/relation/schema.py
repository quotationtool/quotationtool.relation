import zope.interface
import zope.schema

import interfaces


class Relation(zope.schema.Field):
    """See README.txt for documentation."""

    zope.interface.implements(interfaces.IRelation)

    def __init__(self,
                 precondition = interfaces.IRelation['precondition'].default,
                 **kw):
        interfaces.IRelation['precondition'].validate(precondition)
        self.precondition = precondition
        super(Relation, self).__init__(**kw)

    def _validate(self, value):
        super(Relation, self)._validate(value)

        for iface in self.precondition:
            if iface.providedBy(value):
                return

        raise interfaces.RelationPreconditionError
        
    def set(self, object, value):
        """see zope.schema.Object"""
        # Announce that we're going to assign the value to the object.
        # Motivation: Widgets typically like to take care of policy-specific
        # actions, like establishing location.
        event = zope.schema._field.BeforeObjectAssignedEvent(value, self.__name__, object)
        notify(event)
        # The event subscribers are allowed to replace the object, thus we need
        # to replace our previous value.
        value = event.object
        super(Relation, self).set(object, value)

