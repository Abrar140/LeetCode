javascript
/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
 return Promise.all([promise1, promise2]).then(([num1, num2]) => (
num1+ num2 
 )
 )
};