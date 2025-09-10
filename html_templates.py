css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://as1.ftcdn.net/jpg/14/09/15/58/1000_F_1409155820_yjXKM0AnrduYJLbeUcY9p0edh9g8WmWJ.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://as1.ftcdn.net/v2/jpg/14/68/85/28/1000_F_1468852824_R4TS9VECNqNAYduG8Ew86N5CHtnW2yyx.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''