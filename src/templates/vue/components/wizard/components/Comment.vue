<template>
  <div>
    <div class="field">
      <label class="label fw-bold">Comment</label>
      <div class="control">
        <textarea
            class="form-control "
            v-model="commentForm.comment"></textarea>
      </div>
      <p v-if="$v.commentForm.comment.$error" class="help text-danger">This comment is invalid</p>
    </div>
  </div>
</template>

<script>
import {validationMixin} from 'vuelidate'
import {mapGetters} from 'vuex'
import {required} from 'vuelidate/lib/validators'

export default {
  name    : "Comment",
  mixins  : [validationMixin],
  computed: {
    ...mapGetters(['commentForm'])
  },
  data() {
    return {}
  },
  mounted(){
  },
  validations: {
    commentForm: {
      comment: {},
    }
  },
  watch      : {
    $v         : {
      handler: function (val) {
        console.log('aaa')
      }
    }
  }
}
</script>

<style scoped>
.control {
  min-height: 235px;
}
textarea{
  min-height : 204px !important;
}
</style>