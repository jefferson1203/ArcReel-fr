import type enAuth from '../en/auth';

export default {
  'login': 'Connexion',
  'logging_in': 'Connexion en cours…',
  'login_failed': 'Échec de la connexion',
  'username': 'Nom d\'utilisateur',
  'password': 'Mot de passe',
  'login_subtitle': 'Connectez-vous à votre compte',
} satisfies Record<keyof typeof enAuth, string> & Record<string, string>;

