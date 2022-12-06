# KeyWord:Xiaolz,小栗子,单Q,单Q破解,小栗子5.2.1,小栗子开心版
本文档是由TeaBoss_Developer开发和编写<br/>
编写原因:<br/>
因看到之前有人在Discord上卖激活码,然后有位人想让我算算法.<br/>
我就在6分钟以内想出算法并写出初版算法和源码(旧算法,新算法文档目前Private)<br/>
只支持10位QQ以及部分9位<br/>
本源码仅为源破解工程的算法实现,并没有参与任何破解工程.<br/>
一切违法用法与开发者无关,此文档仅为算法实现.<br/>
本源码可能会用到以下PIP支持库:<br/>
1.flask<br/>
2.requests<br/>
other:Python自带<br/>
本源码意义何在:<br/>
我看到咸鱼以及多个平台,付费传播破解码.<br/>
并且一部分是我的文档而出,因此我开源在此处.<br/>
鸣谢:<br/>
小波[提供样本]<br/>
Flask支持库:提供WebAPI<br/>
许可协议:
本源码许可协议为Apache License


算法实现(源贴链接:https://www.iculture.cc/forum-post/28201.html):<br/>
<div class="theme-box wp-posts-content" data-nav="posts"><h2 id="wznav_0">样本取样</h2>
<p>在说明算法之前,我们先看看两个样本.分别是:</p>
<p>2220067959 =&gt; 04778C5384778C53840400778C5384000F</p>
<p>1844002667=&gt;&nbsp; 046B3FE96D6B3FE96D04006B3FE96D000F</p>
<p>大家先看看在这两条样本中,是否含有一种规律.</p>
<h2 id="wznav_1">样本分析</h2>
<p>先看第一个样本 04778C5384778C53840400778C5384000F</p>
<p>04&nbsp; 778C5384&nbsp; 778C5384&nbsp; 0400&nbsp; 778C5384&nbsp; 000F</p>
<p>现在我们发现,样本是由04 子样本 子样本 0400 子样本 000F排列的</p>
<h2 id="wznav_2">子样本分析</h2>
<p>在上文,2220067959生成的样本中,含有778C5384的多次循环.</p>
<p>之前,我以为是某种算法的取值,我尝试了好多算法,并进行比对,但是最后都没能解出来.</p>
<p>但是,我后面一看,这串样本中没有大于F(16进制的最大数).我就向16进制想了想.</p>
<p>在Python中进行Hex(取16进制)运算后,得到以下值</p>
<div class="quote_q quote-mce " mce-contenteditable="false">
<div mce-contenteditable="true">
<p>0x84538c77&nbsp;</p>
</div>
</div>
<p>当我们把0x后面的信息取出来以后,我们能发现取Hex后的值和子样本有关系 778C5384:84538C77</p>
<p>当我们倒着看这个Hex值时,我们就能发现子样本可能是这样排列的:取Hex后[78:56:34:12]其中的数字表示为在Hex结果中第几位数字.</p>
<p>那源Hex进行排序正好是我们需要的子样本”778C5384″</p>
<p>我们用第二个样本检验一下试试</p>
<h2 id="wznav_3">验证思路</h2>
<p>HEX(1844002667)&nbsp; =&gt;&nbsp; 6DE93F6B</p>
<p>我们以上面规律排序 04&nbsp; 6B3FE96D&nbsp; &nbsp;6B3FE96D&nbsp; &nbsp;0400&nbsp; &nbsp;6B3FE96D&nbsp; &nbsp;000F</p>
<p>正好验证了上文我们所求的算法值</p>
<h2 id="wznav_4">算法实现(Python)</h2>
<p>result =&nbsp; <span style="color: var(--main-color)">str(hex([QQ的值]))</span></p>
<div>
<div>buf&nbsp; = &nbsp;a[8:10]+a[6:8]+a[4:6]+a[2:4]&nbsp; &nbsp; #按照子文本规律取值(并删掉0x)</div>
<div>破解码Result = <span style="color: var(--main-color)">str.upper(’04’+result+result+’0400’+result+’000F’)</span></div>
<div>upper:全部小写字母取大写,因为Hex计算后为小写字母.</div>
</div>
<div>&nbsp;</div>
<div>&nbsp;</div>
<h2 id="wznav_5"><strong>最后总结</strong></h2>
<p>这套系统仅为算法实现,一切后果与作者无关.</p>
<p>本源码为Apache License&nbsp; &nbsp;支持二次修改并商用,但是请保留原作者.</p>
<p>最后:大家如果商用,请差不多良心点,这样的东西本来也没多大难度.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<div>
<div>&nbsp;</div>
</div>
</div>
