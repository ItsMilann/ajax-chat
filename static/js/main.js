//getting cookie
function getCookie(name) {
  var cookieValue = null
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";")
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim()
      if (cookie.substring(0, name.length + 1) == name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}
//Scroll
function scrolldown() {
  message_box.scrollTop = message_box.scrollHeight
}
const adminAvatar =
  "https://pickaface.net/gallery/avatar/20151205_194059_2696_Chat.png"

const userAvatar =
  "https://vietplace.com/Portals/0/Upload/avatar6_86142c6e-63e2-4700-89bf-e3804a75526a.png"

function chatMessage(message, float, color, avatarLink) {
  var text = `<p ${float}">
    <img style="height:35px; border-radius:50%; margin-bottom:5px;" src=${avatarLink} alt="" class="shadow">
    <span class="bg-${color} p-1 mb-2 rounded shadow text-light">
      ${message}
    </span>
  </p>`
  return text
}
// AJAX -- GET Messsages
function refreshMessages() {
  const xhr = new XMLHttpRequest()
  xhr.open("POST", "/message_lists/")
  xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
  xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
  xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))
  xhr.responseType = "json"
  xhr.onload = function () {
    var messageArr = xhr.response
    var messageList = messageArr.slice(Math.max(messageArr.length - 10, 0))
    var allMessages = ""
    var i
    for (i = 0; i < messageList.length; i++) {
      if (messageList[i].admin_message !== null) {
        var admin_text = chatMessage(
          messageList[i].admin_message,
          "float-left",
          "primary",
          adminAvatar
        )
      }else{
        var admin_text = ''
      }
      if (messageList[i].client_message !== null) {
        console.log(messageList[i])
        var client_text = chatMessage(
          messageList[i].client_message,
          "float-right",
          "secondary",
          userAvatar
        )
      }else{
        var client_text = ""
      }
      allMessages += client_text
      allMessages += admin_text
    }
    message_box.innerHTML = allMessages
  }
  xhr.send()
  scrolldown()
}
// JS
var message_field = document.getElementById("client_message")
if (message_field === null) {
  var message_field = document.getElementById("admin_message")
}
function send(e) {
  e.preventDefault()
  var formData = new FormData(e.target)
  var xhr = new XMLHttpRequest()
  xhr.open("POST", "")
  xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
  xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
  xhr.onload = function () {
    console.log(xhr.response)
  }
  xhr.send(formData)
  message_field.value = " "
}
const interval = setInterval(refreshMessages, 500)
