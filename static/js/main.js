/**
 * CookBookr - Main JavaScript functionality
 */

// Debug function to check if script is loaded
console.log('CookBookr main.js loaded');

/* ============================================================================
   TAG SELECTOR FUNCTIONALITY
   ============================================================================ */

/**
 * Initialize tag selector functionality
 * Used on add_recipe and edit_recipe pages
 */
function initializeTagSelector() {
    console.log('Initializing tag selector...');
    
    // Find elements
    const tagDropdown = document.getElementById('tag-dropdown');
    const selectedTagsContainer = document.getElementById('selected-tags');
    
    // Try to find the hidden select field with multiple approaches
    let hiddenSelect = document.querySelector('select[name="recipe_tags"]') ||
                       document.getElementById('id_recipe_tags') ||
                       document.getElementById('recipe-tags-select');
    
    console.log('Elements found:', {
        tagDropdown: !!tagDropdown,
        selectedTagsContainer: !!selectedTagsContainer,
        hiddenSelect: !!hiddenSelect
    });
    
    // If any element is missing, exit early
    if (!tagDropdown || !selectedTagsContainer || !hiddenSelect) {
        console.log('Missing elements, tag selector not initialized');
        return;
    }
    
    console.log('All elements found, setting up tag selector');
    
    // Track selected tags
    let selectedTags = new Set();
    
    // Helper function to get tag display name
    function getTagName(value) {
        const option = tagDropdown.querySelector(`option[value="${value}"]`);
        return option ? option.textContent.trim() : value;
    }
    
    // Helper function to update the hidden select field
    function updateHiddenSelect() {
        console.log('Updating hidden select with tags:', Array.from(selectedTags));
        Array.from(hiddenSelect.options).forEach(option => {
            option.selected = selectedTags.has(option.value);
        });
    }
    
    // Helper function to create a tag badge
    function createTagBadge(value, name) {
        const badge = document.createElement('span');
        badge.className = 'tag-badge';
        badge.innerHTML = `
            ${name}
            <button type="button" class="tag-remove" data-tag="${value}" aria-label="Remove ${name} tag">
                ×
            </button>
        `;
        return badge;
    }
    
    // Helper function to render all selected tags
    function renderSelectedTags() {
        console.log('Rendering selected tags:', Array.from(selectedTags));
        selectedTagsContainer.innerHTML = '';
        
        selectedTags.forEach(tagValue => {
            const tagName = getTagName(tagValue);
            const badge = createTagBadge(tagValue, tagName);
            selectedTagsContainer.appendChild(badge);
        });
        
        updateHiddenSelect();
    }
    
    // Event listener for dropdown selection
    tagDropdown.addEventListener('change', function() {
        const selectedValue = this.value;
        console.log('Dropdown changed, selected value:', selectedValue);
        
        if (selectedValue && selectedValue !== '' && !selectedTags.has(selectedValue)) {
            console.log('Adding tag:', selectedValue);
            selectedTags.add(selectedValue);
            renderSelectedTags();
        }
        
        // Reset dropdown
        this.value = '';
    });
    
    // Event listener for tag removal
    selectedTagsContainer.addEventListener('click', function(e) {
        if (e.target.classList.contains('tag-remove')) {
            const tagValue = e.target.getAttribute('data-tag');
            console.log('Removing tag:', tagValue);
            selectedTags.delete(tagValue);
            renderSelectedTags();
        }
    });
    
    // Initialize with existing selections (for edit forms)
    if (hiddenSelect.options) {
        Array.from(hiddenSelect.options).forEach(option => {
            if (option.selected) {
                selectedTags.add(option.value);
            }
        });
    }
    
    // Initial render
    renderSelectedTags();
    
    console.log('Tag selector initialization complete');
}

/* ============================================================================
   DOCUMENT READY INITIALIZATION
   ============================================================================ */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tag selector on recipe forms
    initializeTagSelector();
    // After initializing, render badges for any pre-selected tags
    renderSelectedTags();
    // Add any other initialization functions here as needed
});

// Import global notification utility
// Use window.showNotification for pop-up alerts in recipe form actions