<template>
  <div>
    <div v-for="(title, idx) in titles" :key="idx">
      <p @click="toggle(title)" :class="{ 'completed' : title.complete }">{{ title.title}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  props: {
    titles: Array,
  },
  methods: {
    toggle(item) {
      item.complete = !item.complete
      console.log(item.complete)
    }
  }
}
</script>

<style>
  .completed {
    text-decoration: line-through;
  }

</style>