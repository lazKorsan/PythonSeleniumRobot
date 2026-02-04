var assert = require('assert');
var monica = require('./');

describe('monica', function () {
  it('should sing', function () {
    assert.equal(monica.sing(), 'thanks thanks thanks thanks Monica');
  });
});
