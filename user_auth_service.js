```javascript
const admin = require('firebase-admin');
const serviceAccount = require('./path/to/serviceAccountKey.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();

class UserAuthService {
  constructor() {
    this.db = db;
  }

  async createUser(email, password, role) {
    try {
      const userRecord = await admin.auth().createUser({
        email: email,
        password: password,
        customClaims: {
          role: role,
        },
      });

      console.log('Successfully created new user:', userRecord.uid);
    } catch (error) {
      console.log('Error creating new user:', error);
    }
  }

  async getUser(uid) {
    try {
      const userRecord = await admin.auth().getUser(uid);
      console.log('Successfully fetched user data:', userRecord.toJSON());
      return userRecord;
    } catch (error) {
      console.log('Error fetching user data:', error);
    }
  }

  async updateUser(uid, email, password, role) {
    try {
      const userRecord = await admin.auth().updateUser(uid, {
        email: email,
        password: password,
        customClaims: {
          role: role,
        },
      });

      console.log('Successfully updated user:', userRecord.uid);
    } catch (error) {
      console.log('Error updating user:', error);
    }
  }

  async deleteUser(uid) {
    try {
      await admin.auth().deleteUser(uid);
      console.log('Successfully deleted user');
    } catch (error) {
      console.log('Error deleting user:', error);
    }
  }
}

if (require.main === module) {
  const userAuthService = new UserAuthService();

  // Test create user
  userAuthService.createUser('test@example.com', 'password', 'admin');

  // Test get user
  userAuthService.getUser('testUid');

  // Test update user
  userAuthService.updateUser('testUid', 'updated@example.com', 'newPassword', 'viewer');

  // Test delete user
  userAuthService.deleteUser('testUid');
}
```
