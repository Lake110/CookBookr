let selectedDay = null;
let selectedMeal = null;

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function showNotification(message, type='success') {
  const area = document.getElementById('notification-area');
  area.innerHTML = `
    <div class="alert alert-${type} alert-dismissible fade show" role="alert">
      ${message}
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
  `;
}

// Initialize Bootstrap tooltips for prep time and notes
function initTooltips() {
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl);
  });
}

document.addEventListener('DOMContentLoaded', function() {
  initTooltips();

  // Modal logic for "+ Add Recipe" buttons
  document.querySelectorAll('.open-recipe-modal').forEach(function(btn) {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      var day = btn.getAttribute('data-day');
      var meal = btn.getAttribute('data-meal');
      // Store day/meal info for modal logic
      window.selectedDay = day;
      window.selectedMeal = meal;
      // Open the modal (Bootstrap)
      var recipeModal = new bootstrap.Modal(document.getElementById('recipeModal'));
      recipeModal.show();
    });
  });

  const modal = document.getElementById('addRecipeModal');
  modal.addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget;
    document.getElementById('modal-day').value = button.getAttribute('data-day');
    document.getElementById('modal-meal').value = button.getAttribute('data-meal');
  });
});

// Handle recipe selection

document.querySelectorAll('.select-recipe-btn').forEach(button => {
  button.addEventListener('click', function () {
    const recipeId = this.dataset.recipeId;

    fetch('/mealplanner/assign/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify({
        recipeId: recipeId,
        day: selectedDay,
        meal: selectedMeal
      })
    }).then(response => {
      if (response.ok) {
        showNotification('Recipe assigned successfully!');
        setTimeout(() => location.reload(), 1000);
      } else {
        showNotification('Failed to assign recipe.', 'danger');
      }
    });
  });
});
