export default function guest ({ next, store }) {
  console.log('middleware work')
  if (store.getters['auth/check']) {
    return next({ name: 'home' })
  } else {
    return next()
  }
}
