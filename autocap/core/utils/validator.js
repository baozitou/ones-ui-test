
class ValidationError extends Error {};

// 如果值不为true则抛错
const ensure = (value, msg) => {
  if (!value) {
    throw new ValidationError(msg);
  }
  return value;
};

module.exports = {
  ensure,
  ValidationError
};
