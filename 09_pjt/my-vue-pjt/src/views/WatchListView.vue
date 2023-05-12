<template>  
  <div>
    <WatchListForm @add-title="addTitle"/>
    <WatchListItem :titles="titles"/>
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm'
import WatchListItem from '@/components/WatchListItem'

export default {
  name: 'WatchList',
  data() {
    return {
      titles: [],
    }
  },
  components: {
    WatchListForm,
    WatchListItem,
  },
  methods: {
    addTitle: function(title) {
      this.titles.push(
        {title: title, complete: false}
      )
    }
  },
}
</script>

<style>

</style>