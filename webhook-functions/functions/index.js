const functions = require('firebase-functions');
const request = require('request');

// Create and Deploy Your First Cloud Functions
// https://firebase.google.com/docs/functions/write-firebase-functions

exports.helloWorld = functions.https.onRequest((req, res) => {
    request.get('<server host>')
        .on('response', (result) => {
            return res.send({
                code: result.statusCode
            });
        });
});
