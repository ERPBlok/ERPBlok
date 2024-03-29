import { defineComponent } from 'furetui/src/components/factory';

defineComponent('homepage', {
  template: `
    <div class="container has-text-centered">
      <h1 class="title">ERPBlok</h1>
      <div class="column is-half is-offset-one-quarter">
        <img class="image" v-bind:src="logo" alt="Logo">
      </div>
    </div>
  `,
});
defineComponent('furet-ui-appbar-body', {
  template: `
    <div />
  `,
});
defineComponent('furet-ui-appbar-footer', {
  template: `
    <div />
  `,
});
