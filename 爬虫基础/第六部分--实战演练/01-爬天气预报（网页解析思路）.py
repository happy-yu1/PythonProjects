#以中国天气网为例，爬取某天  每个城市的最低温度，并进行对比

"""
先进行网页解析。共分为八个区，每个区下面有不同的省份，每个省下面又有不同城市
一、分析华北地区
1、华北地区下有北京、天津、东北等，每个省份的信息放在table标签下
<table width="100%" border="0" cellpadding="0" cellspacing="0">
    <tr>……<tr>  #第一个tr
    <tr>……<tr>  #第二个tr
    <tr style="background-color: rgb(255, 255, 255);">  #第三个tr
        <td width="74" rowspan="17" class="rowsPan">
        <a href="/textFC/tianjin.shtml" target="_blank">东北</a>
        </td>
        ……
        <td width="86">-2</td>
       </a></td>
    </tr>
2、以东北为例
某省份下的每个城市的具体信息存放在<tr>……<tr>标签中，第一个和第二个存放的是标题，从第三个tr开始才是每个城市的具体信息，一个tr存放一个城市的相关信息
3、城市最低气温
存放在tr标签下某个的td标签中的文本中

二、进一步分析
因为一周有7天，第一行存放今天的信息，第二行存放明天，依次类推，如果查看今天的天气情况，其他几天的信息就会被隐藏起来：因为style="display:none;"
可以将<div class="conMidtab">提取出来，
<div class="conMidtab"> 这里存放的是华北地区今天的所以信息（是所需的）
<div class="conMidtab" style="display:none;"> 明天的信息
<div class="conMidtab" style="display:none;">
<div class="conMidtab" style="display:none;">
<div class="conMidtab" style="display:none;">
<div class="conMidtab" style="display:none;">
<div class="conMidtab" style="display:none;">
提取完信息后再进一步解析：
<div class="conMidtab">  #存放华北地区的信息
    <div class="conMidtab2"> #存放北京信息
        <table width="100%" border="0" cellpadding="0" cellspacing="0"> #关于table标签的解析如一中所示。
    <div class="conMidtab2"> #存放天津的信息
    <div class="conMidtab2">
    <div class="conMidtab2">

1、先提取出<div class="conMidtab">（今天华北地区所有信息），
2、再提取出<div class="conMidtab2">中的<table width="100%" border="0" cellpadding="0" cellspacing="0"> （某个城市的所有信息）
3、再提取第三个tr标签<tr style="background-color: rgb(255, 255, 255);">
4、再提取tr下的某个所需天气温度的td标签
"""
