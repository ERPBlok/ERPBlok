import { startFuretUI } from 'furetui/src/main';
import { routes } from 'furetui/src/router';
import './components';
import 'vuejs_sensee_backend/components';
import './styles.scss';
import 'vuejs_sensee_backend/styles/app.scss';

startFuretUI('furet-ui-custom', routes);
