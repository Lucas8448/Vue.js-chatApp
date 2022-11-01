<script setup>
import Chat from './components/chat.vue'
</script>

<template>
  <header>
  </header>

  <main>
    <div class="nav">

    </div>
    <div class="chat" v-for="(id, content, addr) in messages">
      <Chat :msg="content" :ip="addr" />
    </div>
    <div class="msg">
      <form action="http://127.0.0.1:5000/msg" method="POST">
        <div>
          <input class="input" name="message" id="message"/>
        </div>
        <div>
          <button class="send">Send</button>
        </div>
      </form>
    </div>
  </main>
</template>

<script>
import axios from 'axios'

export default {
  name: 'home',
  data() {
    return {
      nutrients: {}
    }
  },
  methods: {
    messages: function () {
      axios.get('http://127.0.0.1:5000')
        .then(response => { this.messages = response.data })
    }
  }
}
</script>

<style scoped>
.msg {
  position: absolute;
  height: 100px;
  background-color: #f5f5f5;
  border-top: 1px solid #e5e5e5;
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
