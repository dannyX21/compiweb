const vm = new Vue({
  el: "#app",
  delimiters: ["<%", "%>"],
  data: {
    tokens: [],
    errores: [],
    codigo: ""
  },
  watch: {
    codigo: function(newCodigo, oldCodigo) {
      this.compila();
    }
  },
  methods: {
    compila: _.debounce(
    function(){
      let vm = this;
      axios.post('compila/', {
        codigo: this.codigo
      }).then(function(res) {
        vm.tokens = [].concat(res.data.tokens);
        vm.errores = [].concat(res.data.errores);
      }).catch(function(err) {
        console.log(err);
      });
    }, 1000),
    setFocus: function() {
      this.$refs.codigo.focus();
    }
  }
});
