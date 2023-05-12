<template>
  <div>
    <h1>보고싶은 영화</h1>
    <input type="text" v-model="title" @keyup.enter="titleToParent">
    <button @click="titleToParent">Add</button>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data() {
    return {
      title: '',
    }
  },
  methods: {
    titleToParent: function() {
      this.$emit('add-title', this.title)
      this.title = ''
    },
    toggle() {

    }
  }
}
</script>

<style>

</style>