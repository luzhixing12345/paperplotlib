// 保存所有全局修改的配置


// 美化选择框
// - [ ] xxx
// - [x] aaa
var inputs = document.getElementsByTagName('input')
for(var i=0;i<inputs.length;i++) {
    inputs[i].removeAttribute('disabled')
    inputs[i].onclick = function() {
        return false;
    }
}

var markdown_part = document.querySelector(".markdown-body");


var currentUrl = window.location.href.slice(0, -1);
var dirTree = document.querySelector(".dir-tree");
var links = dirTree.querySelectorAll("a");

// 如果保存的主题存在,则设置当前主题为保存的主题
const savedTheme = localStorage.getItem('theme');
if (savedTheme !== null) {
    if (savedTheme === 'light') {
        markdown_part.className = 'markdown-body markdown-light'
    } else {
        markdown_part.className = 'markdown-body markdown-dark'
    }
}
links.forEach(function(link) {
  if (link.href === currentUrl) {
    link.scrollIntoView({block: 'center', inline:'nearest', container: dirTree });
    if (savedTheme) {
        if (savedTheme == 'dark') {
            link.classList.add("link-active-dark");
        } else {
            link.classList.add("link-active");
        }
    } else {
        link.classList.add("link-active");
    }
  }
});

// 代码段可编辑, 可选中
var code_blocks = document.getElementsByTagName('pre');
for (var i = 0; i < code_blocks.length; i++) {
    code_blocks[i].setAttribute('contenteditable', 'true');
}

document.onkeydown = function (e) {
    // 对于左/右键被按下的情况, 切换至上一页下一页
    if (e.key === "ArrowLeft") {
        // console.log("左箭头键被按下");
        // 找到第一个 change-article 类的 button
        var button = document.querySelector(".change-article");
        if (button.getAttribute('url') !== '.') {
            window.location= button.getAttribute('url')
        }
    } else if (e.key === "ArrowRight") {
        // console.log("右箭头键被按下");
        // 找到最后一个 change-article 类的 button
        var button = document.querySelector(".change-article:last-child");
        if (button.getAttribute('url') !== '.') {
            window.location= button.getAttribute('url')
        }
        
    }
}