import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

const dataState = createPersistedState()
Vue.use(Vuex)


export default new Vuex.Store({
    plugins  : [dataState],
    state    : {
        form             : {
            username : '',
            demoEmail: '',
            message  : ''
        },
        isLoggedIn       : false,
        isRegisterClicked: false,
        parts            : [],
        contactForm      : {
            first_name     : '',
            last_name      : '',
            email          : '',
            phone          : '',
            companyName    : '',
            password       : '',
            confirmPassword: '',
            existUser      : ''
        },
        commentForm      : {
            comment: '',
        },
        submitForm       : {
            quantity: '',
            zip_code: '',
            type    : ''
        }
    },
    mutations: {
        setParts(state, payload) {
            state.parts = payload
        },
        setIsRegisterClicked(state, value) {
            state.isRegisterClicked = value
        },
        setIsLoggedIn(state, value) {
            state.isLoggedIn = value
        },
        setCommentForm(state, payload) {
            state.commentForm = {
                comment: payload,
            }
        },
        setContactForm(state, payload) {
            state.contactForm = payload
        },
        setContactFormExistUser(state, payload) {
            state.contactForm.existUser = payload
        },
        setSubmitForm(state, payload) {
            state.submitForm = payload
        },
        emptyForm(state) {
            state.parts       = []
            state.contactForm = {
                first_name     : '',
                last_name      : '',
                email          : '',
                phone          : '',
                companyName    : '',
                password       : '',
                confirmPassword: '',
                existUser      : ''

            }
            state.commentForm = {
                comment: '',
            }
            state.submitForm  = {
                quantity: '',
                zip_code: '',
                type    : ''
            }
        }
    },
    actions  : {},
    modules  : {},
    getters  : {
        form(state) {
            return state.form;
        },
        getIsLoggedIn(state) {
            return state.isLoggedIn
        },
        getIsRegisterClicked(state) {
            return state.isRegisterClicked
        },
        parts(state) {
            return state.parts;
        },
        contactForm(state) {
            return state.contactForm;
        },
        commentForm(state) {
            return state.commentForm;
        },
        submitForm(state) {
            return state.submitForm;
        }
    }
})
