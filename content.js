if (window.location.pathname === '/gate') {
  window.location.href = '/index';
}

let code = "";
const field = document.getElementById("premium-code");

window.alert = function() {};

const fcc = String.fromCharCode;
String.fromCharCode = function(...args) {
  const result = fcc.apply(this, args);
  if (args.length === 1) code += result;
  return result;
};

if (field && typeof window.validateCode === 'function') {
  window.validateCode();
  field.value = code;
  window.validateCode();
}
