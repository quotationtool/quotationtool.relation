Schema
------

The Relation schema-field is similar to zope.schema.Object. The
difference is, that it does not check if the schema is fullfilled by
the related object. To pass the precondition, the object has to
provide at least one interfaces given.

    >>> from quotationtool.relation.schema import Relation
    >>> import zope.interface

First, let's create some dummy objects implementing some dummy
interfaces.

    >>> class I1(zope.interface.Interface):
    ...     pass
    >>> class I2(zope.interface.Interface):
    ...     pass
    >>> class I3(zope.interface.Interface):
    ...     pass
    >>> class C1:
    ...     zope.interface.implements(I1)

    >>> class C2:
    ...     zope.interface.implements(I2)

    >>> class C3:
    ...     zope.interface.implements(I3)

    >>> o1 = C1()
    >>> o2 = C2()
    >>> o3 = C3()
  


Now we use our new schema field to define an interface.

    >>> class IRelated(zope.interface.Interface):
    ...     relation = Relation(
    ...         title = u"Relation",
    ...         precondition = [I1, I2],
    ...         )

Now we can use the field to validate objects against it:

    >>> IRelated['relation'].validate(o1)
    >>> IRelated['relation'].validate(o3)
    Traceback (most recent call last):
    ...
    RelationPreconditionError
    >>> IRelated['relation'].validate(o2)
