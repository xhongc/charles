$(document).ready(function () {
    /*--------------------搜索框样式控制js------------------------*/
    var search_types = {
        'baidu': {name: "https://www.baidu.com/s?wd=", stype: "/static/moyu/1_scbaidu.png", type: "baidu"},
        'bing': {name: "https://cn.bing.com/search?q=", stype: "/static/moyu/4_scbing.png", type: "bing"},
        'zhihu': {name: "https://www.zhihu.com/search?q=", stype: "/static/moyu/zhihu.ico", type: "zhihu"},
        'google': {name: "https://www.google.com/search?q=", stype: "/static/moyu/6_scgoogle.png", type: "google"},
        'youdao': {name: "https://dict.youdao.com/search?q=", stype: "/static/moyu/youdao.ico", type: "youdao"},
    }
    var checktype = $(".sChoiceBtn");
    var type = $(".scSmallBox");
    var oMsoBtn1 = document.getElementById('msoBtn1');
    var oMsoBigBox = document.getElementById('msoBigBox');
    var oMsoBtn1Img = document.getElementById('msoBtn1Img');
    var oMsoLock = document.getElementById('msoLock');
    var oMsoBigBoxLine1 = document.getElementById('msoBigBoxLine1');

    var seach_type = $(".scBigBox");
    var form = $("#search_bg #button_bg form");
    var textb = $("#search_bg #button_bg form .textb");
    var subb = $("#search_bg #button_bg form .subb");
    var tbcolor = "#126AC1";


    var oSearchText = document.getElementById('search');
    var searchCheck = document.getElementById("searchCheck");
    searchCheck.addEventListener("submit", function (event) {
        var wordCheck = document.getElementsByClassName("textb")[0];

        if (wordCheck.value.length > 0) {
            window.open(textb[0].name + oSearchText.value.replace(/%/g, "%25").replace(/#/g, "%23").replace(/\+/g, "%2B").replace(/\&/g, "%26"));
        }

        event.preventDefault()
        return false;


    });


    var selType = get_cookie("sel"), obj = null;
    $.each(search_types, function (k, v) {
        if (k === selType) {
            obj = v;
        }
    })
    if (obj != null) {
        //form.attr("action",obj.action);改变表单提交位置
        textb.attr("name", obj.name);//改变表单变量名
        checktype.attr("src", obj.stype);//checktype.css({"background":"url("+obj.stype+")"});
    }
    textb.focus();//文档加载完毕 搜索框获取焦点
    //选择搜索类型按钮被点击
    checktype.click(function () {
        seach_type.css({"display": "block", height: 0});
        seach_type.animate({
            height: (type.height()) * type.length,
        }, 300);
    });

    type.click(function () {
        var search_index = $(this).attr('id')
        var type = search_types[search_index].type, exp = null;
        exp = new Date();
        exp.setTime(exp.getTime() + 2592000 * 1000);//过期时间30day
        document.cookie = "sel=" + type + ";path=/;expires=" + exp.toGMTString();
        textb.attr("name", search_types[search_index].name);//改变表单变量名
        checktype.attr("src", search_types[search_index].stype);//checktype.css({"background":"url("+search_types.types[$(this).index()].stype+")"});

        subb.css({"box-shadow": "0 1px 2px " + search_types[search_index].subcolor});
        textb.focus();//编辑框获取焦点*/
        seach_type.animate({
            height: 0,
        }, 100, function () {
            seach_type.css({"display": "none", height: 0});
        });
    });

    textb.focus(function () {

        //
        seach_type.animate({
            height: 0,
        }, 500, function () {
            seach_type.css({"display": "none", height: 0});
        });
    });

    /*-----------------获取关键词js---------------------*/
    var textb = $("#search_bg #button_bg form .textb");
    textb.keyup(function (event) {
        var sousuo = $('#sousuo');
        var hidden_container = $('#hidden_container')
        var a = $('#last_container').find('a[href*="%s"]'.format(textb.val()))
        if(a.length >=1){
            hidden_container.empty();
            hidden_container.append(a.clone())
        }
        else {
            hidden_container.empty();
            sousuo.hide();
        }
        if (textb.val() == "" || textb.val() == " ") {
            return;
        }
        sousuo.show();
        if (event.which != 39 && event.which != 40 && event.which != 37 && event.which != 38 && event.which != 13)
            $.ajax({
                url: "//sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su",
                type: "GET",
                dataType: "jsonp",
                jsonp: 'jsoncallback',
                async: false,
                timeout: 5000,//请求超时
                data: {
                    "wd": textb.val(),
                    "cb": "keydata"
                },
                success: function (json) {
                },
                error: function (xhr) {
                    return;
                }

            });
    });
    //moni
    $('#moni').on('click', function () {
        var exp = new Date();
        var is_moni = 'false'
        exp.setTime(exp.getTime() + 2592000 * 1000);//过期时间30day
        if ($(this).prop('checked')) {
            $('#lil-monster').show();
            is_moni = 'true'
        } else {
            $('#lil-monster').hide();
        }
        document.cookie = "moni=" + is_moni + ";path=/;expires=" + exp.toGMTString();

    })
    //moni 回填
    var setMoni = get_cookie('moni');
    if (setMoni === 'true') {
        $('#lil-monster').show();
        $('#moni').prop('checked', true)
    }

    //moni
    document.getElementById("balloon").onclick = e => {
        document.onmousemove = null;
        onMouseMove(e, "end");
    };
    document.onmousemove = onMouseMove;

    $('.eye').on('click', function () {
        moniTalk('不要戳我眼睛,莫尼~');
    })
    $('#right-hand').on('click', function () {
        moniTalk('爸爸送我的气球,莫尼~')
    })
    $('#left-hand').on('click', function () {
        moniTalk('不要弄破了,莫尼~')
    })
    $('#balloon').on('mousemove', function () {
        moniTalk('不要动我的球,莫尼！', 1)
    })
    //图标
    $('#tubiao').on('click', function () {
        var exp = new Date();
        var is_tubiao = 'false'
        exp.setTime(exp.getTime() + 2592000 * 1000);//过期时间30day
        if ($(this).prop('checked')) {
            $('#last_container img').show()
            is_tubiao = 'true'
        } else {
            $('#last_container img').hide()
        }
        document.cookie = "tubiao=" + is_tubiao + ";path=/;expires=" + exp.toGMTString();
    })
    //bingbg
    $('#bingbg').on('click', function () {
        var exp = new Date();
        var is_bingbg = 'false'
        exp.setTime(exp.getTime() + 2592000 * 1000);//过期时间30day
        if ($(this).prop('checked')) {
            $('.dingbu').css('background-image', 'url(http://area.sinaapp.com/bingImg/)');
            is_bingbg = 'true'
        } else {
            $('.dingbu').css('background-image', 'url("/static/moyu/b1.jpg")');
        }
        document.cookie = "bingbg=" + is_bingbg + ";path=/;expires=" + exp.toGMTString();
    })
    //bingbg 回填
    var setBingbg = get_cookie('bingbg');
    if (setBingbg === 'true') {
        $('.dingbu').css('background-image', 'url(http://area.sinaapp.com/bingImg/)');
        $('#bingbg').prop('checked', true)
    }
});

//moni
function onMouseMove(event, end) {
    const eyes = document.getElementsByClassName("eye");
    for (let i in eyes) {
        const eye = eyes[i];
        if (eye.style) {
            if (end) {
                eye.style.transform = "rotate(190deg)";
            } else {
                const {
                    x, y, width, height
                } = eye.getBoundingClientRect();
                const left = x + width / 2;
                const top = y + height / 2;
                const rad = Math.atan2(event.pageX - left, event.pageY - top);
                const degree = rad * (180 / Math.PI) * -1 + 180;
                eye.style.transform = "rotate(" + degree + "deg)";
            }
        }
    }
}

function moniTalk(content, times = 2) {
    xtip.tips(content, '#moni_msg', {
        bgcolor: '#FFFFFF',
        times: times,
        pos: 'r',
        color: 'black'
    })
}

function get_cookie(Name) {
    var search = Name + "="//查询检索的值
    var returnvalue = "";//返回值
    if (document.cookie.length > 0) {
        sd = document.cookie.indexOf(search);
        if (sd != -1) {
            sd += search.length;
            end = document.cookie.indexOf(";", sd);
            if (end == -1)
                end = document.cookie.length;
            //unescape() 函数可对通过 escape() 编码的字符串进行解码。
            returnvalue = unescape(document.cookie.substring(sd, end))
        }
    }
    return returnvalue;
}

//打印关键词
function keydata(keys) {
    var len = keys.s.length;
    var keywordbox = $("#search_bg #button_bg .keyword");//关键词盒子
    var textb = $("#search_bg #button_bg form .textb");
    var subb = $("#search_bg #button_bg form .subb");
    if (len == 0) {
        keywordbox.css({display: "none"});
    } else {
        keywordbox.css({display: "block"});
    }
    var spans = "";
    for (var i = 0; i < len; i++) {
        spans += "<span>" + keys.s[i] + "</span>"
    }
    keywordbox.html(spans);//把关键词写入关键词盒子
    keywordbox.animate({
        height: (keywordbox.children().height() + 1) * len//关键词下滑效果
    }, 100);
    //点击候选词汇
    keywordbox.children().click(function () {
        textb.val($(this).html());//选中词汇放入输入框

        keywordbox.animate({
            height: 0//关键盒子收缩效果
        }, 10, function () {
            keywordbox.css({display: "none", height: "auto"});
            keywordbox.empty();//清空盒子内容
        });

        textb.focus();//输入框获取焦点*/

        var oSearchText = document.getElementById('search')
        if (textb[0].value) {
            window.open(textb[0].name + oSearchText.value.replace(/%/g, "%25").replace(/#/g, "%23").replace(/\+/g, "%2B").replace(/\&/g, "%26"))
        }//提交搜索
    });

    //提交按钮获取焦点后
    subb.focus(function () {//提交按钮获取焦点后
        keywordbox.animate({
            height: 0//关键盒子收缩效果
        }, 10, function () {
            keywordbox.css({display: "none", height: "auto"});
            keywordbox.empty();//清空盒子内容

        });
    });

    /*textb.blur(function(){//输入框失去焦点后收缩关键词盒子(此方法会与点击候选词方法冲突造成失效)
        keywordbox.animate({
            height:0//关键盒子收缩效果
        },100,function(){
            keywordbox.css({display:"none",height:"auto"});
            keywordbox.empty();//清空盒子内容
        });
    });*/
    /*keywordbox.mouseleave(function(){//鼠标离开关键字盒子后收缩关键词盒子（取代上一个方法）
        keywordbox.animate({
            height:0//关键盒子收缩效果
        },100,function(){
            keywordbox.css({display:"none",height:"auto"});
            keywordbox.empty();//清空盒子内容
        });
    });*/
    var numspan = 0;//用来指定选择候选词（通过方向键改变）
    textb.keydown(function (event) {//如果使用回车提交时，关键词盒子也可以自动收缩
        /*if(event.which==8){//按下Backspace键触发，清空关键词关闭盒子
            if(textb.length==1){
                keywordbox.animate({
                height:0//关键盒子收缩效果
                },10,function(){
                    keywordbox.css({display:"none",height:"auto"});
                    keywordbox.empty();//清空盒子内容
                });
            }
        }*/
        if (event.which == 13) {
            keywordbox.animate({
                height: 0//关键盒子收缩效果
            }, 10, function () {
                keywordbox.css({display: "none", height: "auto"});
                keywordbox.empty();//清空盒子内容
            });
            /*$("#search_bg #button_bg form").submit(function(){
                return false;//阻止提交
            });*/
            /*$("#search_bg #button_bg form").submit(function(e){
                e.preventDefault();//阻止提交方法2
            });*/
        }
        //按下下方向键
        if (event.which == 40) {

            if (numspan == len)
                numspan = 0;
            for (var i = 0; i < len; i++) {
                if (numspan == i) {
                    keywordbox.children().eq(i).css({
                        "background-color": "rgba(149,191,226)"
                    });
                } else {
                    keywordbox.children().eq(i).css({
                        "background-color": "rgba(255,255,255,0.3)"
                    });
                }
            }
            textb.val(keywordbox.children().eq(numspan).html());
            numspan++;
        }
        //按下上方向键
        if (event.which == 38) {

            numspan--;
            if (numspan == len)
                numspan = 0;
            for (var i = 0; i < len; i++) {
                if (numspan == i) {
                    keywordbox.children().eq(i).css({
                        "background-color": "rgba(149,191,226)"
                    });
                } else {
                    keywordbox.children().eq(i).css({
                        "background-color": "rgba(255,255,255,0.3)"
                    });
                }
            }
            textb.val(keywordbox.children().eq(numspan).html());

        }
    });
    keywordbox.children().mouseover(function () {
        numspan = $(this).index();
        for (var i = 0; i < len; i++) {
            if (numspan == i) {
                keywordbox.children().eq(i).css({
                    "background-color": "#f1f1f1"
                });
            } else {
                keywordbox.children().eq(i).css({
                    "background-color": "rgba(255,255,255,0.3)"
                });
            }
        }

    });


    /*点击bg关闭关键词盒子*/
    var oBg = document.getElementsByTagName('body')[0];
    var oSearch = document.getElementById('search');

    oBg.onclick = function () {
        keywordbox.animate({
            height: 0//关键盒子收缩效果
        }, 10, function () {
            keywordbox.css({display: "none", height: "auto"});
            keywordbox.empty();//清空盒子内容
        });
    }
    oSearch.onclick = function (ev) {
        var oEvent = ev || event;
        oEvent.cancelBubble = true;
    }


}
function getDailyContent() {
    $.ajax({
        url:'https://www.mxnzp.com/api/daily_word/recommend?&app_id=yhlrkxpsofduvtjb&app_secret=OXlid3FmY0IrTVRtR1NQYUYyRGs2Zz09',
        type:'get',
        success:function (data) {
            $('.tishi').html(data.data[0].content)
        }
    })
}
function getNana() {
        $.ajax({
            url: '/api/nana/',
            type: 'get',
            success: function (data) {
                var tr_count = 0
                $.each(data, function (k, v) {
                    tr_count += 1
                    var td_count = 0
                    if (tr_count <= 5) {
                        var tr_html = '<tr>\n' +
                            '    <th>\n' +
                            '        %s\n' +
                            '    </th>'
                        tr_html = tr_html.format(v.title)
                    } else {
                        var tr_html = ''
                    }
                    var h1_html = '<h1 id="%s" class="uk-heading-line uk-text-center">\n' +
                        '                <span>\n' +
                        '                    %s\n' +
                        '                </span>\n' +
                        '    </h1>\n' +
                        '<div class="uk-child-width-1-5@m uk-grid-medium uk-grid-match uk-grid" uk-grid="">'
                    h1_html = h1_html.format(v.html_id, v.title)
                    var scroll_nav_html = '<li class="">\n' +
                        '                <a href="#%s">\n' +
                        '                    %s\n' +
                        '                </a>\n' +
                        '            </li>'
                    scroll_nav_html = scroll_nav_html.format(v.html_id, v.title)
                    $('#id_scroll_nav').append(scroll_nav_html)
                    $.each(v.cates, function (k, v) {
                        td_count += 1
                        if (td_count <= 6 && tr_count <= 5) {
                            var td_html = '<td class="uk-table-link">\n' +
                                '        <a class="uk-link-reset" href="%s" target="_blank" nana="%s">\n' +
                                '            %s\n' +
                                '        </a>\n' +
                                '    </td>';
                            td_html = td_html.format(v.url, v.id, v.title)
                            tr_html += td_html
                        }
                        var a_html = '<a href="%s" target="_blank" class="uk-first-column" nana="%s">\n' +
                            '            <div class="uk-card uk-card-default uk-card-hover uk-card-body">\n' +
                            '                <div class="uk-card-media-top">\n' +
                            '                    <img data-src="%s" alt="" src="../static/images/loading.gif" style="height: 120px">\n' +
                            '                </div>\n' +
                            '                <div class="uk-card-body">\n' +
                            '                    <h3 class="uk-card-title">\n' +
                            '                        %s\n' +
                            '                    </h3>\n' +
                            '                    <p>\n' +
                            '                        %s\n' +
                            '                    </p>\n' +
                            '                </div>\n' +
                            '            </div>\n' +
                            '        </a>';
                        a_html = a_html.format(v.url, v.id, v.img_path, v.title, v.description)
                        h1_html += a_html
                    })

                    tr_html += '</tr>'
                    $('.changyong').append(tr_html);


                    h1_html += '</div>'
                    $('#last_container').append(h1_html)

                })
                //图标 回填
                var setTubiao = get_cookie('tubiao');
                if (setTubiao === 'false') {
                    $('#last_container img').hide()
                    $('#tubiao').prop('checked', false)
                }
                start();
            }
        })
    }
