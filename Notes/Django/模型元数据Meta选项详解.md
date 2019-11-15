### Meta选项大致包含以下几类：

**1.abstract**
这个属性是定义当前的模型是不是一个抽象类。所谓抽象类是不会对应数据库表的。一般我们用它来归纳一些公共属性字段，然后继承它的子类可以继承这些字段。
Options.abstract
如果abstract=True这个model就是一个抽象类
**2.app_label**
这个选型只在一种情况下使用，就是你的模型不在默认的应用程序包下的models.py文件中，这时候需要指定你这个模型是哪个应用程序的。
Options.app_label
如果一个model定义在默认的models.py，例如如果你的app的models在myapp.models子模块下，你必须定义app_label让Django知道它属于哪一个app

```
app_label='myapp'
```

**3.db_table**
db_table是指定自定义数据库表名的。Django有一套默认的按照一定规则生成数据模型对应的数据库表明。
Options.db_table
定义该model在数据库中的表名称

```
db_table='Students'
```

如果你想使用自定义的表名，可以通过以下该属性

```
table_name='my_owner_table'
```

**4.db_teblespace**
Options.db_teblespace
定义这个model所使用的数据库表空间。如果在项目的settin中定义那么它会使用这个值
**5.get_latest_by**
Options.get_latest_by
在model中指定一个DateField或者DateTimeField。这个设置让你在使用model的Manager上的lastest方法时，默认使用指定字段来排序
**6.managed**
Options.managed
默认值为True，这意味着Django可以使用syncdb和reset命令来创建或移除对应的数据库。默认值为True,如果你不希望这么做，可以把manage的值设置为False
**7.order_with_respect_to**
这个选项一般用于多对多的关系中，它指向一个关联对象，就是说关联对象找到这个对象后它是经过排序的。指定这个属性后你会得到一个get_xxx_order()和set_xxx_order()的方法，通过它们你可以设置或者回去排序的对象
**8.ordering**
这个字段是告诉Django模型对象返回的记录结果集是按照哪个字段排序的。这是一个字符串的元组或列表，没有一个字符串都是一个字段和用一个可选的表明降序的'-'构成。当字段名前面没有'-'时，将默认使用升序排列。使用'?'将会随机排列

```
ordering=['order_date']#按订单升序排列
ordering=['-order_date']#按订单降序排列，-表示降序
ordering=['?order_date']#随机排序，？表示随机
ordering=['-pub_date','author']#以pub_date为降序，在以author升序排列
```

**9.permissions**
permissions主要是为了在DjangoAdmin管理模块下使用的，如果你设置了这个属性可以让指定的方法权限描述更清晰可读。Django自动为每个设置了admin的对象创建添加，删除和修改的权限。

```
permissions=(('can_deliver_pizzas','Candeliverpizzas'))
```

**10.proxy**
这是为了实现代理模型使用的，如果proxy=True,表示model是其父的代理model
**11.unique_together**
unique_together这个选项用于：当你需要通过两个字段保持唯一性时使用。比如假设你希望，一个Person的FirstName和LastName两者的组合必须是唯一的，那么需要这样设置：

```
unique_together=(("first_name","last_name"),)
```

一个ManyToManyField不能包含在unique_together中。如果你需要验证关联到ManyToManyField字段的唯一验证，尝试使用signal(信号)或者明确指定through属性。
**12.verbose_name**
verbose_name的意思很简单，就是给你的模型类起一个更可读的名字一般定义为中文，我们：
verbose_name="学校"
**13.verbose_name_plural**
这个选项是指定，模型的复数形式是什么，比如：

```
verbose_name_plural="学校"
```

如果不指定Django会自动在模型名称后加一个’s’

#### 一些常见的元信息的例子：

```
class UserInfo(models.Model):
        nid = models.AutoField(primary_key=True)
        username = models.CharField(max_length=32)
        
        class Meta:
            # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
            db_table = "table_name"
            
            # 联合索引
            index_together = [
                ("pub_date", "deadline"),
            ]

            # 联合唯一索引
            unique_together = (("driver", "restaurant"),)
            
            # admin中显示的表名称
            verbose_name
            
            # verbose_name加s
            verbose_name_plural
```

#### 多表关系和参数的例子：

```python
ForeignKey(ForeignObject) # ForeignObject(RelatedField)
        to, # 要进行关联的表名
        to_field=None, # 要关联的表中的字段名称
        on_delete=None, # 当删除关联表中的数据时，当前表与其关联的行的行为
             - models.CASCADE，删除关联数据，与之关联也删除
             - models.DO_NOTHING，删除关联数据，引发错误IntegrityError
             - models.PROTECT，删除关联数据，引发错误ProtectedError
             - models.SET_NULL，删除关联数据，与之关联的值设置为null（前提FK字段需要设置为可空）
             - models.SET_DEFAULT，删除关联数据，与之关联的值设置为默认值（前提FK字段需要设置默认值）
             - models.SET，删除关联数据，
             	a. 与之关联的值设置为指定值，设置：models.SET(值)
             	b. 与之关联的值设置为可执行对象的返回值，设置：models.SET(可执行对象)
                    def func():
                        return 10
                    class MyModel(models.Model):
                        user = models.ForeignKey(
                            to="User",
                            to_field="id"
                            on_delete=models.SET(func),)
        related_name=None,  # 反向操作时，使用的字段名，用于代替 【表名_set】 如： obj.表名_set.all()
        related_query_name=None, # 反向操作时，使用的连接前缀，用于替换【表名】 如： models.UserGroup.objects.filter(表名__字段名=1).values('表名__字段名')
        limit_choices_to=None, # 在Admin或ModelForm中显示关联数据时，提供的条件：
        	# 如：
            - limit_choices_to={'nid__gt': 5}
            - limit_choices_to=lambda : {'nid__gt': 5}
            from django.db.models import Q
            - limit_choices_to=Q(nid__gt=10)
            - limit_choices_to=Q(nid=8) | Q(nid__gt=10)
            - limit_choices_to=lambda : Q(Q(nid=8) | Q(nid__gt=10)) & Q(caption='root')
        db_constraint=True          # 是否在数据库中创建外键约束
        parent_link=False           # 在Admin中是否显示关联数据
```

```python
OneToOneField(ForeignKey)
    to,                         # 要进行关联的表名
    to_field=None               # 要关联的表中的字段名称
    on_delete=None,             # 当删除关联表中的数据时，当前表与其关联的行的行为
    ###### 对于一对一 ######
    # 1. 一对一其实就是 一对多 + 唯一索引
    # 2.当两个类之间有继承关系时，默认会创建一个一对一字段
    # 如下会在A表中额外增加一个c_ptr_id列且唯一：
    class C(models.Model):
        nid = models.AutoField(primary_key=True)
        part = models.CharField(max_length=12)
	class A(C):
        id = models.AutoField(primary_key=True)
        code = models.CharField(max_length=1)
```

```python
ManyToManyField(RelatedField)
    to,                         # 要进行关联的表名
    related_name=None,          # 反向操作时，使用的字段名，用于代替 【表名_set】
    							# 如： obj.表名_set.all()
    related_query_name=None,    # 反向操作时，使用的连接前缀，用于替换【表名】
    	# 如： 
        models.UserGroup.objects.filter(表名__字段名=1).values('表名__字段名')
    limit_choices_to=None,      # 在Admin或ModelForm中显示关联数据时，提供的条件：
        # 如：
        - limit_choices_to={'nid__gt': 5}
        - limit_choices_to=lambda : {'nid__gt': 5}
        from django.db.models import Q
        - limit_choices_to=Q(nid__gt=10)
        - limit_choices_to=Q(nid=8) | Q(nid__gt=10)
        - limit_choices_to=lambda : Q(Q(nid=8) | Q(nid__gt=10)) & Q(caption='root')
    symmetrical=None,  
    	# 仅用于多对多自关联时，symmetrical用于指定内部是否创建反向操作的字段
        # 做如下操作时，不同的symmetrical会有不同的可选字段
        models.BB.objects.filter(...)
        # 可选字段有：code, id, m1
        class BB(models.Model):
            code = models.CharField(max_length=12)
            m1 = models.ManyToManyField('self',symmetrical=True)
        # 可选字段有: bb, code, id, m1
        class BB(models.Model):
            code = models.CharField(max_length=12)
            m1 = models.ManyToManyField('self',symmetrical=False)
    through=None,    # 自定义第三张表时，使用字段用于指定关系表
	through_fields=None, # 自定义第三张表时，使用字段用于指定关系表中那些字段做多对多关系表
        from django.db import models
        class Person(models.Model):
            name = models.CharField(max_length=50)
        class Group(models.Model):
            name = models.CharField(max_length=128)
            members = models.ManyToManyField(
                Person,
                through='Membership',
                through_fields=('group', 'person'),
            )
		class Membership(models.Model):
            group = models.ForeignKey(Group, on_delete=models.CASCADE)
            person = models.ForeignKey(Person, on_delete=models.CASCADE)
            inviter = models.ForeignKey(
                Person,
                on_delete=models.CASCADE,
                related_name="membership_invites",
            )
            invite_reason = models.CharField(max_length=64)
	db_constraint=True,         # 是否在数据库中创建外键约束
    db_table=None,              # 默认创建第三张表时，数据库中表的名称
```

