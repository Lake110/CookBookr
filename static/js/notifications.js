// Global notification utility for all forms
function showNotification(message, type = 'info') {
  const alertDiv = document.createElement('div');
  let alertClass;
  switch(type) {
    case 'success': alertClass = 'alert-success'; break;
    case 'error': alertClass = 'alert-danger'; break;
    case 'info': alertClass = 'alert-info'; break;
    case 'warning': alertClass = 'alert-warning'; break;
    default: alertClass = 'alert-primary';
  }
  alertDiv.className = `alert ${alertClass} alert-dismissible fade show position-fixed top-0 end-0 m-3`;
  alertDiv.role = 'alert';
  alertDiv.innerHTML = `
    ${message}
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  `;
  document.body.appendChild(alertDiv);
  setTimeout(() => {
    alertDiv.classList.remove('show');
    alertDiv.classList.add('hide');
    setTimeout(() => alertDiv.remove(), 500);
  }, 3000);
}
window.showNotification = showNotification;
