import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
	  sum:1
  },
  mutations: {
	  JIA(state,value){
		  state.sum += value
	  }
  },
  actions: {
	  jia(context,value){
		  context.commit('JIA',value)
	  }
  },
  modules: {
  }
})
