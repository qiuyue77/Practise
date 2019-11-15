**API目录**

```text
<1>all():         查询所有结果
<2>filter(**kwargs)    它包含了与所给筛选条件相匹配的对象
<3>get(**kwargs):     返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。
<4>exclude(**kwargs)    它包含了与所给筛选条件不匹配的对象
<5>values(*field)     返回一个ValueQuerySet 一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象，而是一个可迭代的字典序列
<6>values_list(*field)   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
<7>order_by(*field)    对查询结果排序
<8>reverse()        对查询结果反向排序
<9>distinct()       从返回结果中剔除重复纪录
<10>count()        返回数据库中匹配查询(QuerySet)的对象数量。
<11>first()        返回第一条记录
<12>last()         返回最后一条记录
<13>exists()        如果QuerySet包含数据，就返回True，否则返回False
<14>annotate()       使用聚合函数
<15>dates()        根据日期获取查询集
<16>datetimes()      根据时间获取查询集
<17>none()         创建空的查询集
<18>union()        并集
<19>intersection()     交集
<21>difference()      差集
<22>select_related()    附带查询关联对象
<23>prefetch_related()   预先查询
<24>extra()        附加SQL查询
<25>defer()        不加载指定字段
<26>only()         只加载指定的字段
<27>using()        选择数据库
<28>select_for_update()  锁住选择的对象，直到事务结束。
<29>raw()         接收一个原始的SQL查询
```

**1、检索所有对象all()**

使用all()方法，可以获取某张表的所有记录。返回当前QuerySet（或QuerySet子类）的副本。通常用于获取全部QuerySet对象。

```
def orm(requst):
    #获取所有文章，对应SQL：select * from Article
    all_article = models.Article.objects.all()
    print(all_article)
    return HttpResponse('orm')
```

保存之后，我们通过浏览器访问，然后查看 Terminal，看到我们的打印出来的查询结果，一共有四篇文章。

![1.jpg](https://www.django.cn/media/upimg/1_20180819213735_709.jpg)

查询出来的是一个QuerySet的对象。

**2、用filter过滤对象**

filter(**kwargs)
返回满足查询参数的对象集合。
查找的参数（**kwargs）应该满足下文字段查找中的格式。多个参数之间是和AND的关系。

常用例子：

```python
# 大于，>，对应SQL：select * from Article where id > 724
Article.objects.filter(id__gt=724)
# 大于等于，>=，对应SQL：select * from Article where id >= 724
Article.objects.filter(id__gte=724)
# 小于，<，对应SQL：select * from Article where id < 724
Article.objects.filter(id__lt=724)
# 小于等于，<=，对应SQL：select * from Article where id <= 724
Article.objects.filter(id__lte=724)
# 同时大于和小于， 1 < id < 10，对应SQL：select * from Article where id > 1 and id < 10
Article.objects.filter(id__gt=1, id__lt=10)
# 包含，in，对应SQL：select * from Article where id in (11,22,33)
Article.objects.filter(id__in=[11, 22, 33])
# 不包含，not in，对应SQL：select * from Article where id not in (11,22,33)
Article.objects.filter(pub_date__isnull=True)
# 不为空：isnull=False，对应SQL：select * from Article where pub_date is not null
Article.objects.filter(pub_date__isnull=True)
# 匹配，like，大小写敏感，对应SQL：select * from Article where name like '%sre%'，SQL中大小写不敏感
Article.objects.filter(name__contains="sre")
# 匹配，like，大小写不敏感，对应SQL：select * from Article where name like '%sre%'，SQL中大小写不敏感
Article.objects.filter(name__icontains="sre")
# 范围，between and，对应SQL：select * from Article where id between 3 and 8
Article.objects.filter(id__range=[3, 8])
# 以什么开头，大小写敏感，对应SQL：select * from Article where name like 'sh%'，SQL中大小写不敏感
Article.objects.filter(name__startswith='sh')
# 以什么开头，大小写不敏感，对应SQL：select * from Article where name like 'sh%'，SQL中大小写不敏感
Article.objects.filter(name__istartswith='sh')
# 以什么结尾，大小写敏感，对应SQL：select * from Article where name like '%sre'，SQL中大小写不敏感
Article.objects.filter(name__endswith='sre')
# 以什么结尾，大小写不敏感，对应SQL：select * from Article where name like '%sre'，SQL中大小写不敏感
Article.objects.filter(name__iendswith='sre')
# 排序，order by，正序，对应SQL：select * from Article where name = '关键词' order by id
Article.objects.filter(name='关键词').order_by('id')
# 多级排序，order by，先按name进行正序排列，如果name一致则再按照id倒叙排列
Article.objects.filter(name='关键词').order_by('name','-id')
# 排序，order by，倒序，对应SQL：select * from Article where name = '关键词' order by id desc
Article.objects.filter(name='关键词').order_by('-id')
```

**3、查询单一对象 get**

filter方法始终返回的是QuerySets，那怕只有一个对象符合过滤条件，返回的也是包含一个对象的QuerySets，这是一个集合类型对象，你可以简单的理解为Python列表，可迭代可循环可索引。
如果你确定你的检索只会获得一个对象，那么你可以使用get()方法来直接返回这个对象。get返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。

```python
#查询ID=1的文章
Article.objects.get(id=1)
#等同
Article.objects.get(pk=1)
```

**4、查询不匹配条件的对象 exclude**

exclude(**kwargs)

返回一个新的QuerySet，它包含**不**满足给定的查找参数的对象。

查找的参数（**kwargs）应该满足下文字段查找中的格式。多个参数通过AND连接，然后所有的内容放入NOT() 中。

下面的示例**排除**所有created_time晚于2018-7-15**且**headline为“Hello” 的记录：

```python
Article.objects.exclude(created_time__gt=datetime.date(2018,7,15), headline='Hello')
```

下面的示例**排除**所有`pub_date`晚于2005-1-3**或者**headline 为“Hello” 的记录：

```python
Article.objects.exclude(created_time__gt=datetime.date(2018,7,15)).exclude(headline='Hello')
```

**5、查询返回一个字典 values**

返回一个ValueQuerySet，一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象，而是一个可迭代的字典序列。每个字典表示一个对象，键对应于模型对象的属性名称。

例：

```python
#values()与普通的模型对象比较：
def orm(requst):
    article = models.Article.objects.filter(title__startswith='增加')
    article_values = models.Article.objects.filter(title__startswith='增加').values()
    print(article)
    print('----------------------------------------------')
    print(article_values)
    return HttpResponse('orm')
    
#打印结果  
<QuerySet [<Article: 增加标题一>, <Article: 增加标题二>]>
----------------------------------------------
<QuerySet [
{'id': 4, 'title': '增加标题一', 'intro': '', 'category_id': 3, 'body': '增加内容一', 'user_id': 1},
{'id': 6, 'title': '增加标题二', 'intro': '测试增加标题二', 'category_id': 4, 'body': '增加内容二', 'user_id': 2}
 ]>
 
#更多用法：
#不指定字段会获取所有字段的键和值
article_values_all = models.Article.objects.values()
#如果指定字段，每个字典将只包含指定的字段的键/值。
article_values_filter = models.Article.objects.values('id', 'title')

#values()方法还有关键字参数**expressions，这些参数将传递给annotate()注释
from django.db.models.functions import Lower
article_values=models.Article.objects.values(标题=Lower('title'))
<QuerySet [{'标题': '增加标题一'}, {'标题': '我被修改了'}, {'标题': '增加标题二'}]>

#聚合应用，统计作者下的文章数量
from django.db.models import Count
article_values_annotate = models.Article.objects.values('user').annotate(数量=Count('title'))
<QuerySet [{'user': 1, '数量': 3}, {'user': 2, '数量': 2}]>

#如果你有一个字段category是一个ForeignKey，默认的category_id参数返回的字典中将有一个叫做category的键，
#因为这是保存实际值的那个隐藏的模型属性的名称
#当调用category_id并传递字段的名称，传递category或values()都可以，得到的结果是相同的。
#像这样：
category=models.Article.objects.values('category')
category_id = models.Article.objects.values('category_id')
<QuerySet [{'category': 3}, {'category': 3}, {'category': 4}, {'category': 4}, {'category': 4}]>
<QuerySet [{'category_id': 3}, {'category_id': 3}, {'category_id': 4}, {'category_id': 4}, {'category_id': 4}]>
```

**6、查询返回一个元组 values_list**

values_list(*fields, flat=False)
与values()类似，只是在迭代时返回的是元组而不是字典。每个元组包含传递给values_list()调用的相应字段或表达式的值，因此第一个项目是第一个字段等。

看例子：

```python
from django.db.models.functions import Lower
values_list=models.Article.objects.values_list('id','title')
values_list_lower = models.Article.objects.values_list('id', Lower('title'))
<QuerySet [(3, 'virtualenv使用技巧大全'), (4, '增加标题一'), (5, '我被修改了'), (6, '增加标题二')]>
<QuerySet [(3, 'virtualenv使用技巧大全'), (4, '增加标题一'), (5, '我被修改了'), (6, '增加标题二')]>
```

如果只传递一个字段，还可以传递flat参数。 如果为True，它表示返回的结果为单个值而不是元组。 如下所示：

```python
values_list=models.Article.objects.values_list('id').order_by('id')
values_list_flat = models.Article.objects.values_list('id', flat=True).order_by('id')
<QuerySet [(2,), (3,), (4,), (5,), (6,)]>
<QuerySet [2, 3, 4, 5, 6]>
```

如果有多个字段，传递flat将发生错误。

**7、查询返回一个元组 order_by**

order_by(*fields)
默认情况下，根据模型的Meta类中的ordering属性对QuerySet中的对象进行排序

```python
article = models.Article.objects.filter(created_time__year=2018).order_by('-created_time', 'title')
```

上面的结果将按照created_time降序排序，然后再按照title升序排序。"-created_time"前面的负号表示降序顺序。 升序是默认的。 要随机排序，使用"?"，如下所示：

```python
article = models.Article.objects.order_by('?')
```

注：order_by('?')可能耗费资源且很慢，这取决于使用的数据库。

若要按照另外一个模型中的字段排序，可以使用查询关联模型的语法。即通过字段的名称后面跟两个下划线（__），再加上新模型中的字段的名称，直到希望连接的模型。

```python
article = models.Article.objects.order_by('category__name', 'title')
```

如果排序的字段与另外一个模型关联，Django将使用关联的模型的默认排序，或者如果没有指定Meta.ordering将通过关联的模型的主键排序。 例如，因为Blog模型没有指定默认的排序：

```python
article = models.Article.objects.order_by('category')
#等于:
article = models.Article.objects.order_by('category__id')
```

如果Blog设置了ordering = ['name']，那么第一个QuerySet将等同于：

```python
article = models.Article.objects.order_by('category__name')
```

还可以通过调用表达式的desc()或者asc()方法：

```python
article = models.Article.objects.order_by(Coalesce('summary', 'title').desc())
```

**8、对查询结果反向排序 reverse**

反向排序QuerySet中返回的元素。 第二次调用reverse()将恢复到原有的排序。
如要获取QuerySet中最后三个元素，可以这样做：

```python
my_queryset.reverse()[:3]
```

这与Python直接使用负索引有点不一样。 Django不支持负索引，只能曲线救国。

**9、从返回结果中剔除重复纪录 distinct**

distinct(*fields)
去除查询结果中重复的行。
默认情况下，QuerySet不会去除重复的行。当查询跨越多张表的数据时，QuerySet可能得到重复的结果，这时候可以使用distinct()进行去重。

**10、返回数据库中匹配查询(QuerySet)的对象数量 count**

返回一个整数，该整数表示数据库中与QuerySet匹配的对象的数量。

**例子：**

```python
#返回数据库中的条目总数
article = models.Article.objects.count()
#返回标题中包含“增加”的条目数
article_filter = models.Article.objects.filter(title__contains='增加').count()
```

count()调用在幕后执行SELECT count(*)，因此您应该始终使用count()，而不是将所有记录加载到Python对象中，然后对结果调用len()(除非无论如何都需要将对象加载到内存中，在这种情况下，len()会更快)。
注意，如果您想要查询一个QuerySet中的项目数量，并且正在从它检索模型实例(例如，通过遍历它)，那么使用len(QuerySet)可能会更高效，因为它不会像count()那样导致额外的数据库查询。

**11、返回由queryset匹配的第一个对象 first\**()\****

返回由queryset匹配的第一个对象，如果没有匹配的对象，则返回None。如果QuerySet没有定义任何排序，那么QuerySet将由主键自动排序。

**例子：**

```python
p = models.Article.objects.order_by('title', 'created_time').first()
#文章的'上一页'就是通过这个实现的
previous_blog = Article.objects.filter(created_time__gt=article_obj.created_time).first()
```

注意，first()是一种简洁的写法，下面的代码示例与上面的示例等价:

```python
try:
    p = models.Article.objects.order_by('title', 'created_time')[0]
except IndexError:
    p = None
```

**12、返回最后一条记录last()**

与first()类似，它是返回queryset中的最后一个对象。

```python
#文章下一页
netx_blog = Article.objects.filter(created_time__lt=article_obj.created_time).last()
```

**13、是否存在记录exists()** 

如果QuerySet包含数据，就返回True，否则返回False  ---只判断是否有记录

如果 `QuerySet` 包含任何结果，则返回 `True`，否则返回 `False`。这尽可能以最简单和最快的方式执行查询，但它确实执行与普通 `QuerySet` 查询几乎相同的查询。

`exists()` 对于与 `QuerySet` 中的对象成员资格以及 `QuerySet` 中的任何对象（特别是大型 `QuerySet` 的上下文）中存在的相关搜索都很有用。

查找具有唯一字段（例如 `primary_key`）的模型是否为 `QuerySet` 的成员的最有效方法是：

```python
entry = Entry.objects.get(pk=123)
if some_queryset.filter(pk=entry.pk).exists():
    print("Entry contained in queryset")
```

这将比以下要求更快，需要对整个查询集进行评估和迭代：

```python
if entry in some_queryset:
    print("Entry contained in QuerySet")
```

查找查询集是否包含任何项目：

```python
if some_queryset.exists():
    print("There is at least one object in some_queryset")
```

这将比以下更快：

```python
if some_queryset:
    print("There is at least one object in some_queryset")
```

...但不是很大程度上（因此需要大量查询来提高效率）。

**14、使用提供的聚合表达式查询对象annotate()**

函数原型annotate(*args, **kwargs)，返回QuerySet。

表达式可以是简单的值、对模型（或任何关联模型）上的字段的引用或者聚合表达式（平均值、总和等）。

annotate()的每个参数都是一个annotation，它将添加到返回的QuerySet每个对象中。

关键字参数指定的Annotation将使用关键字作为Annotation 的别名。 匿名参数的别名将基于聚合函数的名称和模型的字段生成。 只有引用单个字段的聚合表达式才可以使用匿名参数。 其它所有形式都必须用关键字参数。

例如，如果正在操作一个Blog列表，你可能想知道每个Blog有多少Entry：

```bash
>>> from django.db.models import Count
>>> q = Blog.objects.annotate(Count('entry'))# The name of the first blog
>>> q[0].name
'Blogasaurus'# The number of entries on the first blog
>>> q[0].entry__count
42
```

Blog模型本身没有定义`entry__count`属性，但是通过使用一个关键字参数来指定聚合函数，可以控制Annotation的名称：

```bash
>>> q = Blog.objects.annotate(number_of_entries=Count('entry'))
# The number of entries on the first blog, using the name provided
>>> q[0].number_of_entries
35
```

**15、根据日期获取查询集dates()** 

dates(field, kind, order='ASC')

返回一个QuerySet，表示QuerySet内容中特定类型的所有可用日期的`datetime.date`对象列表。

field参数是模型的DateField的名称。 kind参数应为"year"，"month"或"day"。 结果列表中的每个datetime.date对象被截取为给定的类型。

"year" 返回对应该field的所有不同年份值的列表。

"month"返回字段的所有不同年/月值的列表。

"day"返回字段的所有不同年/月/日值的列表。

order参数默认为'ASC'，或者'DESC'。 它指定如何排序结果。

例子：

```bash
>>> Entry.objects.dates('pub_date', 'year')
[datetime.date(2005, 1, 1)]
>>> Entry.objects.dates('pub_date', 'month')
[datetime.date(2005, 2, 1), datetime.date(2005, 3, 1)]
>>> Entry.objects.dates('pub_date', 'day')
[datetime.date(2005, 2, 20), datetime.date(2005, 3, 20)]
>>> Entry.objects.dates('pub_date', 'day', order='DESC')
[datetime.date(2005, 3, 20), datetime.date(2005, 2, 20)]
>>> Entry.objects.filter(headline__contains='Lennon').dates('pub_date', 'day')
[datetime.date(2005, 3, 20)]
```

**16、根据时间获取查询集datetimes()**

datetimes(field_name, kind, order='ASC', tzinfo=None)

返回QuerySet，为datetime.datetime对象的列表，表示QuerySet内容中特定种类的所有可用日期。

`field_name`应为模型的DateTimeField的名称。

kind参数应为"hour"，"minute"，"month"，"year"，"second"或"day"。

结果列表中的每个datetime.datetime对象被截取到给定的类型。

order参数默认为'ASC'，或者'DESC'。 它指定如何排序结果。

tzinfo参数定义在截取之前将数据时间转换到的时区。

**17、 创建空的查询集none()**

调用none()将创建一个不返回任何对象的查询集，并且在访问结果时不会执行任何查询。

例子：

```bash
>>> Entry.objects.none()
<QuerySet []>
>>>> from django.db.models.query import EmptyQuerySet
>>> isinstance(Entry.objects.none(), EmptyQuerySet)
True
```

**18、并集union()**

union(*other_qs, all=False)

Django中的新功能1.11。也就是集合中并集的概念！

使用SQL的UNION运算符组合两个或更多个QuerySet的结果。例如：

```bash
>>> qs1.union(qs2, qs3)
```

默认情况下，UNION操作符仅选择不同的值。 要允许重复值，请使用all=True参数。

**19、交集intersection()**

intersection(*other_qs)

Django中的新功能1.11。也就是集合中交集的概念！

使用SQL的INTERSECT运算符返回两个或更多个QuerySet的共有元素。例如：

```bash
>>> qs1.intersection(qs2, qs3)
```

**21、差集difference()**

difference(*other_qs)

Django中的新功能1.11。也就是集合中差集的概念！

使用SQL的EXCEPT运算符只保留QuerySet中的元素，但不保留其他QuerySet中的元素。例如：

```bash
>>> qs1.difference(qs2, qs3)
```

**22、附带查询关联对象select_related()**

select_related(*fields)

沿着外键关系查询关联的对象的数据。这会生成一个复杂的查询并引起性能的损耗，但是在以后使用外键关系时将不需要再次数据库查询。

下面的例子解释了普通查询和`select_related()`查询的区别。 下面是一个标准的查询：

```python
# 访问数据库。
e = Entry.objects.get(id=5)
# 再次访问数据库以得到关联的Blog对象。
b = e.blog
```

下面是一个`select_related`查询：

```python
# 访问数据库。
e = Entry.objects.select_related('blog').get(id=5)
# 不会访问数据库，因为e.blog已经在前面的查询中获得了。
b = e.blog
```

`select_related()`可用于objects任何的查询集：

```python
from django.utils import timezone

# Find all the blogs with entries scheduled to be published in the future.
blogs = set()

for e in Entry.objects.filter(pub_date__gt=timezone.now()).select_related('blog'):
    # 没有select_related()，下面的语句将为每次循环迭代生成一个数据库查询,以获得每个entry关联的blog。
    blogs.add(e.blog)
```

`filter()`和`select_related()`的顺序不重要。 下面的查询集是等同的：

```python
Entry.objects.filter(pub_date__gt=timezone.now()).select_related('blog')
Entry.objects.select_related('blog').filter(pub_date__gt=timezone.now())
```

可以沿着外键查询。 如果有以下模型：

```python
from django.db import models
class City(models.Model):
    # ...
    pass
class Person(models.Model):
    # ...
    hometown = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
class Book(models.Model):
    # ...
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
```

调用`Book.objects.select_related('author__hometown').get(id=4)`将缓存相关的Person 和相关的City：

```python
b = Book.objects.select_related('author__hometown').get(id=4)
p = b.author         # Doesn't hit the database.
c = p.hometown       # Doesn't hit the database.
b = Book.objects.get(id=4) # No select_related() in this example.
p = b.author         # Hits the database.
c = p.hometown       # Hits the database.
```

在传递给`select_related()`的字段中，可以使用任何ForeignKey和OneToOneField。

在传递给`select_related`的字段中，还可以反向引用OneToOneField。也就是说，可以回溯到定义OneToOneField 的字段。 此时，可以使用关联对象字段的`related_name`，而不要指定字段的名称。

**23、预先查询prefetch_related()**

prefetch_related(*lookups)

在单个批处理中自动检索每个指定查找的相关对象。

与`select_related`类似，但是策略是完全不同的。

假设有这些模型：

```python
from django.db import models
class Topping(models.Model):
    name = models.CharField(max_length=30)
class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):              # __unicode__ on Python 2
        return "%s (%s)" % (
            self.name,
            ", ".join(topping.name for topping in self.toppings.all()),
        )
```

并运行：

```bash
>>> Pizza.objects.all()
["Hawaiian (ham, pineapple)", "Seafood (prawns, smoked salmon)"...
```

问题是每次QuerySet要求`Pizza.objects.all()`查询数据库，因此`self.toppings.all()`将在`Pizza Pizza.__str__()`中的每个项目的Toppings表上运行查询。

可以使用`prefetch_related`减少为只有两个查询：

```bash
>>> Pizza.objects.all().prefetch_related('toppings')
```

这意味着现在每次`self.toppings.all()`被调用，不会再去数据库查找，而是在一个预取的QuerySet缓存中查找。

还可以使用正常连接语法来执行相关字段的相关字段。 假设在上面的例子中增加一个额外的模型：

```python
class Restaurant(models.Model):
    pizzas = models.ManyToManyField(Pizza, related_name='restaurants')
    best_pizza = models.ForeignKey(Pizza, related_name='championed_by')
```

以下是合法的：

```bash
>>> Restaurant.objects.prefetch_related('pizzas__toppings')
```

这将预取所有属于餐厅的比萨饼，和所有属于那些比萨饼的配料。 这将导致总共3个查询 - 一个用于餐馆，一个用于比萨饼，一个用于配料。

```bash
>>> Restaurant.objects.prefetch_related('best_pizza__toppings')
```

这将获取最好的比萨饼和每个餐厅最好的披萨的所有配料。 这将在3个表中查询 - 一个为餐厅，一个为“最佳比萨饼”，一个为一个为配料。

当然，也可以使用`best_pizza`来获取`select_related`关系，以将查询数减少为2：

```bash
>>> Restaurant.objects.select_related('best_pizza').prefetch_related('best_pizza__toppings')
```

**24、附加SQL查询extra()**

extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)

有些情况下，Django的查询语法难以简单的表达复杂的WHERE子句，对于这种情况,可以在extra()生成的SQL从句中注入新子句。使用这种方法作为最后的手段，这是一个旧的API，在将来的某个时候可能被弃用。仅当无法使用其他查询方法表达查询时才使用它。

例如：

```bash
>>> qs.extra(
...     select={'val': "select col from sometable where othercol = %s"},
...     select_params=(someparam,),
... )
```

相当于：

```bash
>>> qs.annotate(val=RawSQL("select col from sometable where othercol = %s", (someparam,)))
```

**25、不加载指定字段defer()**

defer(*fields)

在一些复杂的数据建模情况下，模型可能包含大量字段，其中一些可能包含大尺寸数据（例如文本字段），将它们转换为Python对象需要花费很大的代价。

当最初获取数据时不知道是否需要这些特定字段的情况下，如果正在使用查询集的结果，可以告诉Django不要从数据库中检索它们。

通过传递字段名称到defer()实现不加载：

```python
Entry.objects.defer("headline", "body")
```

具有延迟加载字段的查询集仍将返回模型实例。

每个延迟字段将在你访问该字段时从数据库中检索（每次只检索一个，而不是一次检索所有的延迟字段）。

可以多次调用defer()。 每个调用都向延迟集添加新字段：

```python
# 延迟body和headline两个字段。
Entry.objects.defer("body").filter(rating=5).defer("headline")
```

字段添加到延迟集的顺序无关紧要。对已经延迟的字段名称再次defer()没有问题（该字段仍将被延迟）。

可以使用标准的双下划线符号来分隔关联的字段，从而加载关联模型中的字段：

```python
Blog.objects.select_related().defer("entry__headline", "entry__body")
```

如果要清除延迟字段集，将None作为参数传递到defer()：

```python
# 立即加载所有的字段。
my_queryset.defer(None)
```

defer()方法（及其兄弟，only()）仅适用于高级用例，它们提供了数据加载的优化方法。

**26、只加载指定的字段only()**

only(*fields)

only()方法与defer()相反。

如果有一个模型几乎所有的字段需要延迟，使用only()指定补充的字段集可以使代码更简单。

假设有一个包含字段biography、age和name的模型。 以下两个查询集是相同的，就延迟字段而言：

```python
Person.objects.defer("age", "biography")
Person.objects.only("name")
```

每当你调用only()时，它将替换立即加载的字段集。因此，对only()的连续调用的结果是只有最后一次调用的字段被考虑：

```python
# This will defer all fields except the headline.
Entry.objects.only("body", "rating").only("headline")
```

由于defer()以递增方式动作（向延迟列表中添加字段），因此你可以结合only()和defer()调用：

```python
# Final result is that everything except "headline" is deferred.
Entry.objects.only("headline", "body").defer("body")
# Final result loads headline and body immediately (only() replaces any
# existing set of fields).
Entry.objects.defer("body").only("headline", "body")
```

当对具有延迟字段的实例调用save()时，仅保存加载的字段。

**27、选择数据库using()**

using(alias)

如果正在使用多个数据库，这个方法用于指定在哪个数据库上查询QuerySet。方法的唯一参数是数据库的别名，定义在DATABASES。

例如：

```bash
# queries the database with the 'default' alias.
>>> Entry.objects.all()
# queries the database with the 'backup' alias
>>> Entry.objects.using('backup')
```

**28、锁住选择的对象，直到事务结束。select_for_update()** 
select_for_update(nowait=False, skip_locked=False)

返回一个锁住行直到事务结束的查询集，如果数据库支持，它将生成一个`SELECT ... FOR UPDATE`语句。

例如：

```python
entries = Entry.objects.select_for_update().filter(author=request.user)
```

所有匹配的行将被锁定，直到事务结束。这意味着可以通过锁防止数据被其它事务修改。

一般情况下如果其他事务锁定了相关行，那么本查询将被阻塞，直到锁被释放。使用`select_for_update(nowait=True)`将使查询不阻塞。如果其它事务持有冲突的锁,那么查询将引发`DatabaseError`异常。也可以使用`select_for_update(skip_locked=True)`忽略锁定的行。nowait和`skip_locked`是互斥的。

目前，postgresql，oracle和mysql数据库后端支持`select_for_update()`。但是，MySQL不支持nowait和`skip_locked`参数。

**29、接收一个原始的SQL查询raw()**

raw(raw_query, params=None, translations=None)

接收一个原始的SQL查询，执行它并返回一个`django.db.models.query.RawQuerySet`实例。

这个RawQuerySet实例可以迭代，就像普通的QuerySet一样。