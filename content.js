const form = document.querySelector('form');
const input = form.querySelector('input[name="code"]');
if (form && input) {
  input.value = 'https://www.ely.gg/';
  if (document.referrer !== window.location.href) form.submit();
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
