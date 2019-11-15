#### 在Django中有三种继承风格：
1、如果你想用父类来保存每个子类共有的信息，并且这个类是不会被独立使用的，那么应该使用**抽象基类**。
2、如果你继承现有model(甚至可能这个类是在另一个应用程序中)，并希望每个model都拥有自己对应的数据库，那就应该使用**多表继承**。
3、如果你只是想修改model的Python-level行为，而不改变modelsfields，则使用**代理模式**。 



#### 一、抽象基类-Abstract base classes

当您想要将一些公共信息放入许多其他模型时，抽象基类非常有用。编写基类并在Meta类中放置abstract=True。然后，此模型将不用于创建任何数据库表。相反，当它用作其他模型的基类时，其字段将添加到子类的字段中。
一个例子：

```python
from django.db import models
class CommonInfo (models.Model):
    name = models.CharField (max_length = 100)
    age = models.PositiveIntegerField()
    class Meta :
        abstract = True
        
class Student (CommonInfo):
    home_group = models.CharField (max_length = 5)
```

Student模型将包含三个字段：name，age和home_group。CommonInfo模型不能用作普通的Django模型，因为它是一个抽象基类。它不生成数据库表或具有管理器，并且无法直接实例化或保存。从抽象基类继承的字段可以用另一个字段或值覆盖，或者使用None删除。对于许多用途，这种类型的模型继承将完全符合您的要求。它提供了一种在Python级别分解公共信息的方法，同时仍然只在数据库级别为每个子模型创建一个数据库表。

**1、Meta继承-Meta inheritance**

当创建抽象基类时，Django使您在基类中声明的任何Meta内部类可用作属性。如果子类没有声明自己的Meta类，它将继承父类的Meta。如果孩子想要扩展父类的Meta类，它可以将其子类化。例如：

```python
from django.db import models
class CommonInfo(models.Model):
    # ...
    class Meta :
        abstract = True
        ordering = ['name']
        
class Student(CommonInfo):
    # ...
    class Meta (CommonInfo.Meta):
        db_table = 'student_info'
```

Django确实对抽象基类的Meta类进行了一次调整：在安装Meta属性之前，它设置abstract=False。这意味着抽象基类的子项本身不会自动成为抽象类。当然，您可以创建一个继承自另一个抽象基类的抽象基类。你只需要记住每次都明确设置abstract=True。
在抽象基类的Meta类中包含一些属性是没有意义的。例如，包括db_table意味着所有子类（未指定自己的Meta）将使用相同的数据库表，这几乎肯定不是您想要的。

**2、related_name和related_query_name**

如果在ForeignKey或ManyToManyField上使用ForeignKey或ManyToManyField，则必须始终为该字段指定唯一的反向名称和查询名称。这通常会导致抽象基类出现问题，因为此类中的字段包含在每个子类中，每次都具有完全相同的属性值（包括related_name和related_query_name）。
要解决此问题，当您在抽象基类（仅）中使用related_name或'%(app_label)s'，该值的一部分应包含'%(app_label)s'和'%(class)s'。
'%(class)s'替换为使用该字段的子类的低级别名称。
'%(app_label)s'被包含在子类中的应用程序的低级名称替换。每个安装的应用程序名称必须是唯一的，并且每个应用程序中的模型类名称也必须是唯一的，因此生成的名称最终会有所不同。
例如，给定一个app common/models.py：

```python
from django.db import models
class Base (models.Model):
    m2m = models.ManyToManyField (
        OtherModel ,
        related_name = " %(app_label)s _ %(class)s _related" ,
        related_query_name = " %(app_label)s _ %(class)s s" ,
    )
    class Meta :
        abstract = True
class ChildA (Base):
    pass
class ChildB (Base):
    pass
```

与另一个app rare/models.py ：

```python
from common.models import Base
class ChildB(Base):
    pass
```

示例中，common.ChildA.m2m字段的反向名称为common_childa_related，反向查询名称为common_childas。common.ChildB.m2m字段的反向名称为common_childb_related，反向查询名称为common_childbs。最后，rare.ChildB.m2m字段的反向名称将为rare_childb_related，反向查询名称将为rare_childbs。由你如何使用'%(class)s'和'%(app_label)s'部分来构造你的相关名称或相关的查询名称，但如果你忘了使用它，Django会在你执行系统检查时引发错误（或运行migrate）。
如果没有为抽象基类中的字段指定related_name属性，则默认反向名称将是子类的名称，后跟'_set'，就像通常直接声明字段一样在子类-上。例如，在上面的代码中，如果省略了childa_set属性，则m2m字段的反向名称将是ChildA案例中的ChildB和ChildA字段中的ChildB。

#### 二、多表继承-Multi-table inheritance

Django支持的第二种模型继承是当层次结构中的每个模型都是模型本身时。每个模型对应于自己的数据库表，可以单独查询和创建。继承关系引入子模型与其每个父模型之间的链接（通过自动创建的OneToOneField）。例如：

```python
from django.db import models
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
```

所有Place的字段都可以在Restaurant中使用，虽然数据存放在不同的数据表中。所以可以如下使用：

```bash
>>> Place.objects.filter(name="Bob'sCafe")
>>> Restaurant.objects.filter(name="Bob'sCafe")
```

如果一个Place对象存在相应的Restaurant对象，那么就可以使用Place对象通过关系获得Restaurant对象：

```bash
>>> p = Place.objects.get(id=12)
# If p is a Restaurant object, this will give the child class:
>>> p.restaurant
<Restaurant: ...>
```

但是，如果上面的示例中的p不是Restaurant（它已直接创建为Place对象或是其他类的父对象），则引用p.restaurant会引发一个Restaurant.DoesNotExist异常。
在Restaurant上自动创建的OneToOneField将其链接到Place如下所示：

```python
place_ptr = models.OneToOneField(
    Place,on_delete=models.CASCADE,
    parent_link=True,
   )
```

**1、Meta和多表继承-Meta and multi-table inheritance**

在多表继承的情况下继承父类的Meta是没有意义的。所有的Meta都已经被应用到父类，再应用这些Meta只会导致矛盾。

所以子model不能访问到父model的Meta，然而也有少数的情况下，子model会从父model中继承一些行为，例如子model没有指定 ordering或 get_latest_by属性，那么就会从父model中继承。

如果父model中有一个排序，但你不希望子model有任何的排序规划，你可以明确的禁用：

```python
class ChildModel(ParentModel):
    # ...
    class Meta:
        # Remove parent's ordering effect
        ordering = []
```

**2、继承和反向关系-Inheritance and reverse relations**

因为多表继承实际是隐式的使用OneToOneField来键接父Model和子model,在这种关系有可能会使用父model来调用子model，比如上面的例子。但是如果你把ForeignKey和ManyToManyField关系应用到这样一个继承关系中，Django会返回一个验证错误，必须要指定一个related_name字段属性。
例如上面的例子，我们再创建一个子类，其中包含一个到父model的ManyToManyField关系字段：

```python
class Supplier(Place):
    customers = models.ManyToManyField(Place)
```

这时会产生一个错误：

```bash
Reverse query name for 'Supplier.customers' clashes with reverse query
name for 'Supplier.place_ptr'.
HINT: Add or change a related_name argument to the definition for'Supplier.customers' or 'Supplier.place_ptr'.
```

解决这个问题只需要在customers字段属性中增加related_name属性：

```python
models.ManyToManyField(Place, related_name='provider')
```

**3、指定父链接字段-Specifying the parent link field**
如上所述，Django会自动创建一个OneToOneField链接你的子model和任何非抽象父model。如果你想自定义子model键接回父model的属性名称，你可以创建自己的OneToOneField并设置parent_link=True，表示这个字段是对父model的回链。

**三、代理模型-Proxy models**

当使用多表继承时一个新的数据表model会在每一个子类中创建，这是因为子model需要存储父model不存在的一些数据字段。但有时只需要改变model的操作行为，可能是为了改变默认的管理行为或添加新的方法。

这时就应该使用代理模式的继承：创建原始model的代理。你可以创建一个用于 create, delete 和 update的代理model,使用代理model的时候数据将会真实保存。这和使用原始model是一样的，所不同的是当你改变model操作时，不需要去更改原始的model。

代理模式的声明和正常的继承声明方式一样。你只需要在Meta class 中定义proxy为True就可以了。

例如，你想为Person model添加一个方法：

```python
from django.db import models
class Person (models.Model ):
    first_name = models.CharField ( max_length = 30 )
    last_name = models.CharField ( max_length = 30 )
    
class MyPerson ( Person ):
    class Meta :
        proxy = True
    def do_something ( self ):
        # ...
        pass
```

MyPerson这个类将作用于父类Person所对应的真实数据表。可通过MyPerson进行所有相应的操作：

```bash
>>> p = Person.objects.create(first_name="foobar")
>>> MyPerson.objects.get(first_name="foobar")
<MyPerson: foobar>
```

你也可以使用代理模式来定义model的不同默认排序，例如：

```python
class OrderedPerson(Person):
    class Meta:
        ordering = ["last_name"]
        proxy = True
```

这样当使用原始model查询时结果是无序的，而使用OrderedPerson进行查询时将按last_name进行排序。

#### 1、QuerySets still return the model that was requested（QuerySets的类型依然会是原始model类型）

当你通过MyPerson来查询Person对象时，返回的QuerySet依然会是Person对象类型的集合。使用代理模式的model是依靠原始model的,是原始model的扩展。而不是用来替代父model。

#### 2、Base class restrictions（基类限制）

代理model必须继承一个非抽像model。

不能从多个非抽像model继承，代理模式不能为不同model之间创建链接。

代理模式可以从任意没有定义字段的抽象model继承。

#### 3、代理模型管理器-Proxy model managers

如果没有指定代理model的管理器(managers)，它将继承父类的管理行为。如果你定义了代理model的管理器,它将会成为默认的，当然父类中定义的任何管理器仍然是可以使用的。

继续上面的例了，增加一个默认的管理器：

```python
from django.db import models
class NewManager(models.Manager):
    # ...
    pass
class MyPerson(Person):
    objects = NewManager()    
    class Meta:
        proxy = True
```

可以通过创建一个含有新的管理器并进行继承，来增加一个新的管理器，而不需要去改变更有的默认管理器。

```python
# Create an abstract class for the new manager.
class ExtraManagers(models.Model):
    secondary = NewManager()    
    class Meta:
        abstract = True
class MyPerson(Person, ExtraManagers):
    class Meta:
        proxy = True
```

#### 4、Differences between proxy inheritance and unmanaged models

代理model看起来很像一个在Meta class中设置了managed的非托管模式model。但实际上这两种方案是不太一样，应该考虑在不同的情况下使用那一个：

两者区别在于：你可以设置model的Meta.managed=False以及通过Meta.db_table指定数据表有创建非托管模式model,并对其添加各种方法，但如果你可保持非托管模式和真实数据表之间的同步，做任何更改都将是很麻烦的事。

而代理model主要用于管理model的各种行为或方法，他们将继承父model的管理器等。

曾经尝试将两种模式合并，但由于API会变得非常复杂，并且难以理解，所以现在是分离成两种模式：

一般的使用规划是：

1、如果正使用现有的数据表，但不想在Django中镜像所有的列，所以应该使用Meta.managed=False，通过这个选项使不在django控制下的数据表或视图是可用的。

2、如果你想改变一个model的操作行为，但希望保持原始model不被改变，就应该使用Meta.proxy=True.

### 四、Multiple inheritance(多重继承)

和Python的继承方式一样，django中的model也可以从多个父model继承，当然也和Python的继承方式 一样，如果出现相同名字的时候只有第一个将被使用。例如：如果多个父model中都包含Meta类，将只有第一个将被使用，其他会被忽略。

通常情况下是不会用到多重继承的。主是用于“混合式”model:增加一个特殊的额外字段或方式是由多个父model组合而来。应该尽量保持继承层次的简单，不然会很难排查某个信息是从那里来的。

在django1.7以前，多个父model中有id主键字段时虽然不会引发错误，但有可能导致数据的丢失。例如像下面的model:

```python
class Article(models.Model):
    article_id=models.AutoField(primary_key=True)
    # ...
    pass
class Book(models.Model):
    book_id=models.AutoField(primary_key=True)
    # ...
    pass
class BookReview(Book,Article):
    pass
```

或者使用共同的祖先来保持AutoField。这需要使用OneToOneField从每个父模型到共同祖先的显式来避免子项自动生成和继承的字段之间的冲突：

```python
class Piece(models.Model):
    pass
class Article(Piece):
    article_piece=models.OneToOneField(Piece,on_delete=models.CASCADE,parent_link=True)
    # ...
    pass
class Book(Piece):
    book_piece=models.OneToOneField(Piece,on_delete=models.CASCADE,parent_link=True)
    # ...
    pass
classBookReview(Book,Article):
    pass
```

**1、Fieldname“hiding”isnotpermitted**
正常的Python类继承，允许一个子类覆盖父类的任何属性。在Django中是不允许覆盖父类的属性字段的。如果一个父类中定义了一个叫author的字段，你就不能在子model中创建别一个叫author的字段。
这种限制仅适用于字段（field），普通的python属性是可以的。也有一种情况是可以覆盖的:多表继承的时候进行手动指定数据库列名，可以出现子model和父model有同名的字段名称，因为他们属于不同的数据表。
如果你覆盖了父model的字段属性，django会抛出FieldError异常。