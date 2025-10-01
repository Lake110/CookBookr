// Custom JavaScript for CookBookr

document.addEventListener('DOMContentLoaded', function() {
    console.log('CookBookr loaded successfully!');
    
    // Auto-trigger dashboard modal for authenticated users (only once per session)
    const dashboardModal = document.getElementById('dashboardModal');
    if (dashboardModal && !sessionStorage.getItem('dashboardModalShown')) {
        // Show modal after a short delay for better UX
        setTimeout(() => {
            const modal = new bootstrap.Modal(dashboardModal);
            modal.show();
            // Mark as shown for this session
            sessionStorage.setItem('dashboardModalShown', 'true');
        }, 1500);
    }
    
    // Add smooth scrolling to anchor links
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ 
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add loading animation for recipe cards
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        card.classList.add('fade-in');
    });
    
    // Enhanced recipe card interactions
    cards.forEach(card => {
        // Add click-to-expand functionality for truncated descriptions
        const cardText = card.querySelector('.card-text');
        if (cardText && cardText.textContent.includes('...')) {
            cardText.style.cursor = 'pointer';
            cardText.title = 'Click to expand description';
            
            cardText.addEventListener('click', function() {
                if (this.classList.contains('expanded')) {
                    this.classList.remove('expanded');
                    this.style.webkitLineClamp = '3';
                } else {
                    this.classList.add('expanded');
                    this.style.webkitLineClamp = 'unset';
                }
            });
        }
        
        // Add loading state for recipe view buttons (but NOT form submit buttons)
        const viewButton = card.querySelector('.btn-primary');
        if (viewButton && !viewButton.closest('form')) { // Only if not inside a form
            viewButton.addEventListener('click', function(e) {
                // Only add loading state if it's a real link (not just #)
                if (this.getAttribute('href') !== '#') {
                    this.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status"></span>Loading...';
                    this.disabled = true;
                } else {
                    e.preventDefault();
                    showNotification('Recipe detail page coming soon!', 'info');
                }
            });
        }
    });
    
    // Bootstrap tooltip initialization
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Modal enhancements
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        // Add escape key handler
        modal.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                const modalInstance = bootstrap.Modal.getInstance(this);
                if (modalInstance) {
                    modalInstance.hide();
                }
            }
        });
        
        // Add click outside to close (optional enhancement)
        modal.addEventListener('click', function(e) {
            if (e.target === this) {
                const modalInstance = bootstrap.Modal.getInstance(this);
                if (modalInstance) {
                    modalInstance.hide();
                }
            }
        });
    });
    
    // Add search functionality (for future implementation)
    const searchInput = document.querySelector('#recipeSearch');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                filterRecipes(this.value);
            }, 300);
        });
    }
    
    // Add console log for debugging
    console.log(`Found ${cards.length} recipe cards on this page`);
    
    // Welcome message for new users
    if (!localStorage.getItem('returningUser')) {
        setTimeout(() => {
            if (!document.querySelector('.modal.show')) { // Don't show if modal is already open
                showNotification('Welcome to CookBookr!', 'success');
            }
            localStorage.setItem('returningUser', 'true');
        }, 2000);
    }
});

// Utility function for notifications
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = `
        top: 20px; 
        right: 20px; 
        z-index: 9999; 
        min-width: 300px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    `;
    
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
    
    console.log(`${type.toUpperCase()}: ${message}`);
}

// Recipe filtering function (for search functionality)
function filterRecipes(searchTerm) {
    const cards = document.querySelectorAll('.card');
    const term = searchTerm.toLowerCase();
    
    cards.forEach(card => {
        const title = card.querySelector('.card-title').textContent.toLowerCase();
        const description = card.querySelector('.card-text').textContent.toLowerCase();
        const author = card.querySelector('small').textContent.toLowerCase();
        
        if (title.includes(term) || description.includes(term) || author.includes(term)) {
            card.parentElement.style.display = 'block';
        } else {
            card.parentElement.style.display = 'none';
        }
    });
    
    // Show "no results" message if no cards visible
    const visibleCards = document.querySelectorAll('.card[style="display: block"], .card:not([style*="display: none"])').length;
    if (visibleCards === 0 && searchTerm.length > 0) {
        showNotification(`No recipes found for "${searchTerm}"`, 'warning');
    }
}