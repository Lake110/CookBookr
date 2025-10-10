# CookBookr

A social media-style recipe sharing website built with Django where users can create, share, and discover recipes while engaging with a vibrant culinary community through comments and interactions.

🌐 **Live Site**: [https://cookbookr-75c0f1b11cd0.herokuapp.com/](https://cookbookr-75c0f1b11cd0.herokuapp.com/)

## Table of Contents

- [UX Design](#ux-design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
- [User Stories and Kanban Board](#user-stories-and-kanban-board)
- [Wireframes](#wireframes)
- [ERD Diagram](#erd-diagram)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
- [How AI Was Used](#how-ai-was-used)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Code Validation](#code-validation)
  - [Known Issues](#known-issues)
- [Deployment](#deployment)
- [Credits and Acknowledgements](#credits-and-acknowledgements)

---

## UX Design

CookBookr was designed with a warm, inviting aesthetic that evokes the comfort and joy of home cooking while maintaining modern web standards and accessibility.

### Colour Scheme

The color palette was carefully chosen to create a warm, friendly atmosphere that encourages users to share their culinary creations:

#### Primary Colors
- **Bootstrap Primary (#0D6EFD)**: Used for buttons, links, and primary UI elements
- **Bootstrap Success (#198754)**: Used for positive actions and confirmations
- **Bootstrap Warning (#FFC107)**: Used for alerts and important notices
- **Bootstrap Danger (#DC3545)**: Used for delete actions and error states

#### Supporting Colors
- **White (#FFFFFF)**: Main background for clean, readable interface
- **Light Gray (#F8F9FA)**: Card backgrounds and subtle sections
- **Dark Gray (#212529)**: Primary text for excellent readability
- **Medium Gray (#6C757D)**: Secondary text and meta information

#### Color Psychology
The clean, modern color scheme was selected to:
- Ensure excellent readability and accessibility
- Create a professional, trustworthy appearance
- Allow food photography to be the visual focus
- Maintain consistency with modern web design standards

### Typography

Typography choices emphasize readability and modern design:

- **Primary Font**: System font stack for optimal performance
- **Headings**: Bold weights (font-weight: 600-700) for clear hierarchy
- **Body Text**: Regular weight (font-weight: 400) with 1.5 line height
- **Recipe Instructions**: Clear, structured lists with adequate spacing
- **Meta Information**: Smaller text (0.9rem) for cooking times and author info

### Imagery

- **Recipe Images**: Cloudinary-hosted images with responsive sizing
- **Placeholder Images**: Clean default images when user photos aren't available
- **Icons**: FontAwesome icons for consistent, recognizable UI elements
- **Layout**: Card-based design for easy scanning and visual organization

---

## User Stories and Kanban Board

### Epic: User Authentication & Account Management

#### User Story 1: Register and Log In *(must-have)*
**As a site user, I can register and log in so that I can share my own recipes.**

**Acceptance Criteria:**
- **AC1:** Users can register with email/username and password
- **AC2:** Users can log in with correct credentials
- **AC3:** Users receive appropriate error messages for invalid credentials

**Status:** ✅ **Completed**

#### User Story 2: User Profile Management *(must-have)*
**As a logged-in user, I can view my profile and see my recipes so that I can manage my content.**

**Acceptance Criteria:**
- **AC1:** Users can see their username in the navigation
- **AC2:** Users can access logout functionality
- **AC3:** User sessions are properly managed

**Status:** ✅ **Completed**

### Epic: Recipe Management

#### User Story 3: Create a Recipe *(must-have)*
**As a logged-in user, I can create a recipe so that I can share it with others.**

**Acceptance Criteria:**
- **AC1:** Users can add title, ingredients, instructions, and image
- **AC2:** Form validation prevents submission of incomplete recipes
- **AC3:** Created recipes appear in the recipe list

**Status:** ✅ **Completed**

#### User Story 4: View Recipes *(must-have)*
**As a site visitor, I can view recipes so that I can try cooking them.**

**Acceptance Criteria:**
- **AC1:** All users can browse recipes without logging in
- **AC2:** Recipe details show all necessary cooking information
- **AC3:** Recipes display author, creation date, and cooking details

**Status:** ✅ **Completed**

#### User Story 5: Edit/Delete My Recipes *(must-have)*
**As a recipe author, I can edit or delete my own recipes so that I can keep them up to date.**

**Acceptance Criteria:**
- **AC1:** Only recipe authors can edit their recipes
- **AC2:** Only recipe authors can delete their recipes
- **AC3:** Confirmation is required for destructive actions

**Status:** ✅ **Completed**

### Epic: Community Interaction

#### User Story 6: Comment on Recipes *(must-have)*
**As a logged-in user, I can comment on recipes so that I can give feedback or ask questions.**

**Acceptance Criteria:**
- **AC1:** Logged-in users can add comments to any recipe
- **AC2:** Comments display author name and timestamp
- **AC3:** Comments require login to post

**Status:** ✅ **Completed**

#### User Story 7: Manage My Comments *(must-have)*
**As a comment author, I can edit or delete my own comments so that I can control what I post.**

**Acceptance Criteria:**
- **AC1:** Users can edit their own comments inline
- **AC2:** Users can delete their own comments
- **AC3:** Only comment authors can modify their comments

**Status:** ✅ **Completed**

---

### Epic: Meal Planning & Shopping

#### User Story 8: Add recipes to a weekly meal plan *(should-have)*
**As a site user, I can add recipes to a weekly meal plan so that I can plan my meals ahead.**

**Acceptance Criteria:**
- **AC1:** Given I am logged in, when I click "Add to Meal Plan" on a recipe and select a date/meal type, then the recipe is added to my plan.
- **AC2:** Given I have added recipes, when I view my plan, then I see them assigned to the correct day and meal type.

**Status:** 🚧 **Planned**

#### User Story 9: View calendar-like meal plan *(should-have)*
**As a site user, I can view a calendar-style plan so that I can track what I will cook.**

**Acceptance Criteria:**
- **AC1:** Given I have recipes in my meal plan, when I view the plan page, then I see a weekly calendar layout with meals assigned.
- **AC2:** Given no recipes are in my meal plan, when I view the calendar, then I see an empty weekly view.

**Status:** 🚧 **Planned**

#### User Story 10: Generate shopping list *(could-have)*
**As a site user, I can generate a shopping list from my weekly meal plan so that I know what ingredients to buy.**

**Acceptance Criteria:**
- **AC1:** Given I have recipes in my plan, when I click "Generate Shopping List," then all recipe ingredients are compiled into a list.
- **AC2:** Given I update my meal plan, when I regenerate the list, then the shopping list reflects the changes.

**Status:** 🚧 **Planned**

#### User Story 11: Download shopping list *(could-have)*
**As a site user, I can download my shopping list so that I can use it while shopping.**

**Status:** 🚧 **Planned**

#### User Story 12: View nutrition info *(could-have)*
**As a site user, I can view nutrition info for recipes so that I can track my diet.**

**Acceptance Criteria:**
- **AC1:** Given a recipe has nutrition data, when I open its detail page, then calories, protein, carbs, and fat are displayed.
- **AC2:** Given a recipe does not have nutrition data, when I view it, then I see a message saying "Nutrition information not available."

**Status:** 🚧 **Planned**

#### User Story 13: Import recipes from an external API *(could-have)*
**As a site user, I can import recipes from an external API so that I have more variety in my meal plan.**

**Acceptance Criteria:**
- **AC1:** Given I search for recipes, when the API responds, then I see a list of external recipes.
- **AC2:** Given I view an imported recipe, when I click "Add to Meal Plan," then it is saved in my plan like a local recipe.

**Status:** 🚧 **Planned**

---

## Wireframes

Visual design wireframes for CookBookr across devices:

### Mobile Design (320px - 768px)
![Phone Wireframe](<docs/Readme/images/Phone Design.jpg>)
*Mobile-first approach with touch-friendly buttons and collapsible navigation*

### Tablet Design (768px - 1024px)
![Tablet Wireframe](<docs/Readme/images/Tablet Design.jpg>)
*Optimized for tablet viewing with improved layout spacing*

### Desktop Design (1024px+)
![PC Wireframe](<docs/Readme/images/PC design.jpg>)
*Full desktop experience with expanded navigation and content areas*

**Design Decisions:**
- Mobile-first responsive design approach
- Card-based layout for easy recipe browsing
- Consistent navigation across all screen sizes
- Bootstrap framework for responsive grid system

---

## ERD Diagram

### Database Schema Design

#### Current Implementation (MVP)
![MVP ERD](<docs/Readme/images/Screenshot 2025-09-24 at 15.34.05 copy.png>)

**Current Models:**
- **User**: Django's built-in User model with authentication
- **Recipe**: Core recipe model with title, ingredients, instructions, image, cooking details
- **Comment**: User comments with moderation capability

**Model Relationships:**
- User → Recipe (One-to-Many): Users can create multiple recipes
- User → Comment (One-to-Many): Users can make multiple comments
- Recipe → Comment (One-to-Many): Recipes can have multiple comments

#### Future Enhancements
![Complete ERD](<docs/Readme/images/Overall Project ERD copy.png>)
*Planned database expansion for additional features*

---

## Features

### Existing Features

#### 🏠 **Homepage & Navigation**
- **Responsive Bootstrap navigation** with user authentication status
- **Featured recipes section** showing 4 random recipes
- **Recipe statistics** showing total recipes and community members
- **Mobile-optimized responsive design**

#### 👤 **User Authentication (Django Allauth)**
- **User registration** with email verification disabled for development
- **Login/logout functionality** with session management
- **Secure authentication** with CSRF protection
- **User-specific content** (only show edit/delete for own content)

#### 📝 **Recipe Management**
- **Create recipes** with title, ingredients, instructions, cooking time, servings
- **Image upload** via Cloudinary integration
- **Edit own recipes** with pre-populated forms using Crispy Forms
- **Delete recipes** with confirmation prompts
- **Recipe detail views** with formatted display
- **Author attribution** and timestamp tracking
- **Tag-Based Filtering**: Use tags like "30-minute meals", "family-friendly", "budget-friendly" to find suitable recipes (now implemented)

#### 💬 **Comment System**
- **Add comments** to recipes (authenticated users only)
- **Edit own comments** with inline editing functionality
- **Delete comments** with confirmation
- **Comment moderation** system for content control
- **Author-only edit/delete permissions**

#### 🎨 **UI/UX Features**
- **Bootstrap 5** responsive design framework
- **Crispy Forms** for enhanced form styling
- **FontAwesome icons** for consistent UI elements
- **Django messages** for user feedback (displayed as Bootstrap alerts)
- **Form validation** with helpful error messages
- **Mobile-first responsive design**

#### 🔐 **Security Features**
- **CSRF protection** on all forms
- **User permission checks** for edit/delete operations
- **Django authentication** system
- **Input validation** and sanitization
- **Secure file upload** via Cloudinary

### Features Left to Implement

#### 🍽️ **Meal Planning System**
- **Weekly Meal Calendar**: Interactive calendar interface for planning 7 days of meals
- **Drag & Drop Planning**: Easily drag recipes onto specific days and meal times (breakfast, lunch, dinner)
- **Category-Based Planning**: Filter recipes by categories (vegetarian, quick meals, comfort food, etc.) for targeted meal selection
- **Nutritional Balance**: Visual indicators to help balance meals across the week
- **Shopping List Generation**: Automatically compile ingredients from planned meals into a shopping list
- **Meal Prep Suggestions**: Identify recipes that can be prepared in advance
- **Calendar Export**: Export meal plans to external calendar applications
- **Recipe Suggestions**: AI-powered suggestions based on dietary preferences and previous meal plans
- **Portion Planning**: Adjust recipe servings based on household size and leftover preferences
- **Homepage Integration**: Persistent meal plan sidebar showing current week's planned meals

**Implementation Vision:**

The meal planning interface would feature a clean, calendar-style layout optimized for weekly meal organization:

**Header Section:**
- Week navigation with date range display (e.g., "Week of: Oct 7-13, 2025")
- Action buttons for saving meal plans and exporting to external calendars
- Quick access to meal planning tools and settings

**Main Calendar Grid:**
- **7-column layout** representing days of the week (Monday through Sunday)
- **3-row structure** for each day covering all meal times:
  - **Breakfast row** (B:) - Morning meal planning
  - **Lunch row** (L:) - Midday meal planning  
  - **Dinner row** (D:) - Evening meal planning
- **Interactive cells** where users can drag and drop or click to add recipes
- **Visual recipe cards** showing recipe names, prep times, and thumbnail images
- **Empty state indicators** with clear "[+Recipe]" prompts for adding meals

**Recipe Browser Sidebar:**
- **Filter panel** with category tags (Vegetarian, Quick Meals, Family-Friendly, Budget)
- **Search functionality** to find specific recipes
- **Draggable recipe cards** that can be moved into calendar slots
- **Recipe details preview** on hover or click

**Bottom Action Panel:**
- **Weekly overview** showing nutritional balance and meal variety
- **Shopping list generator** button to compile ingredients
- **Meal prep suggestions** highlighting make-ahead opportunities
- **Calendar sync options** for exporting to Google Calendar, Apple Calendar, etc.

**Homepage Meal Plan Sidebar:**

A collapsible sidebar would appear on the right side of the homepage, providing users with quick access to their current meal plan:

**Sidebar Structure:**
- **Compact week view** showing the next 7 days in a vertical layout
- **Today's meals** highlighted with a distinctive border or background color
- **Meal thumbnails** showing small recipe images for planned meals
- **Quick actions** including "View Full Planner" and "Edit Today's Meals"
- **Grocery reminder** notification if shopping list needs attention

**Sidebar Functionality:**
- **Auto-collapse** on mobile devices to save screen space
- **Persistent across pages** so users can always see their meal plan
- **Click-through navigation** to detailed recipe pages
- **Drag-and-drop integration** allowing users to add featured recipes directly to meal slots
- **Status indicators** showing meal prep reminders and cooking times

**Homepage Integration Benefits:**
- **Quick meal reference** without navigating away from main content
- **Seamless recipe discovery** by dragging homepage recipes into the meal plan
- **Daily meal reminders** keeping users engaged with their planning
- **Cross-feature connectivity** linking recipe browsing with meal planning
- **Reduced navigation friction** for frequent meal plan users

**Responsive Behavior:**
- **Desktop view** (1200px+): Full sidebar always visible alongside main content
- **Tablet view** (768px-1199px): Collapsible sidebar that overlays content when expanded
- **Mobile view** (<768px): Bottom-anchored floating action button that expands to show meal plan
- **Touch optimization** with larger tap targets and swipe gestures for navigation

This integrated approach transforms the homepage from a simple recipe browser into a comprehensive meal planning dashboard, encouraging daily engagement and making meal planning a central part of the user experience rather than a separate feature.

#### 🔍 **Search & Discovery**
- Recipe search functionality (implemented)
- Category filtering and tags (implemented)
- Advanced search with multiple criteria (implemented)
- Recipe recommendations (planned)

#### ⭐ **Social Features**
- Recipe rating system
- User profiles with recipe collections
- Following other users
- Recipe favorites/bookmarks

#### 🖼️ **Media Enhancements**
- Multiple image uploads per recipe
- Image galleries and carousels
- Video recipe tutorials
- Better image optimization

#### 📱 **Technical Enhancements**
- Progressive Web App (PWA) capabilities
- Recipe scaling (adjust servings)
- Print-friendly recipe layouts
- Recipe import from URLs
- Nutritional information display

---

## Technologies Used

### Backend Technologies
- **Python 3.12** - Core programming language
- **Django 4.2+** - Web framework for rapid development
- **PostgreSQL** - Production database (Heroku)
- **SQLite** - Development database
- **Django ORM** - Database abstraction layer
- **Django Allauth** - Authentication system

### Frontend Technologies
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with custom properties
- **JavaScript ES6+** - Interactive functionality
- **Bootstrap 5** - CSS framework for responsive design
- **FontAwesome** - Icon library
- **Crispy Forms** - Enhanced Django form rendering

### Cloud Services & Deployment
- **Heroku** - Cloud platform for deployment
- **Cloudinary** - Image storage and optimization
- **WhiteNoise** - Static file serving
- **Git/GitHub** - Version control

### Development Tools
- **VS Code** - Primary development environment
- **GitHub Copilot** - AI-powered coding assistance
- **Chrome DevTools** - Frontend debugging
- **Heroku CLI** - Deployment management

---

## How AI Was Used

AI tools were strategically integrated throughout the development process to enhance productivity and learning:

### 🧠 **GitHub Copilot Integration**
- **Code Completion**: Accelerated Django view and model development
- **Template Generation**: Assisted with Bootstrap component implementation
- **JavaScript Logic**: Helped implement comment editing functionality
- **CSS Styling**: Suggested responsive design patterns
- **Documentation**: Generated comprehensive code comments

### 💡 **Problem Solving with AI**
- **Debugging Support**: Identified deployment issues (case sensitivity)
- **Configuration Help**: Resolved Heroku deployment challenges
- **Best Practices**: Validated Django patterns and security implementations
- **Performance Tips**: Optimized database queries and static file handling

### 🎓 **Learning Enhancement**
- **Concept Explanation**: AI explained complex Django concepts
- **Code Review**: Identified potential improvements and issues
- **Testing Strategies**: Suggested comprehensive testing approaches
- **Security Guidance**: Reinforced security best practices

### ⚖️ **Maintaining Human Control**
- **Code Review**: All AI suggestions were manually reviewed and tested
- **Business Logic**: Core application logic was human-designed
- **User Experience**: UX decisions based on human judgment
- **Security**: Critical security features manually implemented and validated

---

## Testing

### Manual Testing

#### 🔐 **Authentication Testing**
- User registration: Account is created and user is logged in. Status: Pass.
- User login: User is authenticated and redirected to home. Status: Pass.
- User logout: User is logged out and redirected appropriately. Status: Pass.
- Invalid login: Error message is displayed for incorrect credentials. Status: Pass.

#### 📝 **Recipe Management Testing**
- Create recipe: Recipe is saved and displayed. Status: Pass.
- Edit own recipe: Recipe is updated successfully. Status: Pass.
- Delete own recipe: Recipe is removed with confirmation. Status: Pass.
- View recipe detail: All information is displayed correctly. Status: Pass.
- Form validation: Required fields are enforced. Status: Pass.
- Image upload: Images are stored via Cloudinary. Status: Pass.

#### 💬 **Comment System Testing**
- Add comment (logged in): Comment is saved and displayed. Status: Pass.
- Add comment (not logged in): User is redirected to login page. Status: Pass.
- Edit own comment: Comment is updated inline. Status: Pass.
- Delete own comment: Comment is removed. Status: Pass.
- Comment permissions: Only authors can edit or delete their comments. Status: Pass.

#### 📱 **Responsive Design Testing**
- Mobile (320px-768px): Layout is responsive and navigation uses a collapsible menu. Status: Pass.
- Tablet (768px-1024px): Layout is responsive and navigation is fully accessible. Status: Pass.
- Desktop (1024px+): Layout is responsive and navigation is fully accessible. Status: Pass.

### Code Validation


### Known Issues

#### 🚧 **Current Limitations**
- **Debug Mode**: Currently set to `False` for production, may hide detailed error information
- **Static Files**: Occasional 404 errors for CSS/JS files in production (resolved with collectstatic)
- **Image Upload**: Limited file size validation for Cloudinary uploads
- **Search**: No search functionality currently implemented

#### 🔄 **Planned Fixes**
- Implement comprehensive error logging
- Add file size validation for uploads
- Improve static file handling in production
- Add search and filtering capabilities

---

## Deployment

### 🚀 **Local Development Setup**

1. **Clone the Repository**
```bash
git clone https://github.com/lake110/cookbookr.git
cd cookbookr
```

2. **Create Virtual Environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Setup**
Create `config/env.py`:
```python
SECRET_KEY = 'your-secret-key-here'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

5. **Database Setup**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

6. **Run Development Server**
```bash
python manage.py runserver
```

### 🌐 **Production Deployment (Heroku)**

1. **Prerequisites**
- Heroku account created
- Heroku CLI installed
- Git repository initialized

2. **Heroku App Creation**
```bash
heroku create cookbookr-75c0f1b11cd0
heroku git:remote -a cookbookr-75c0f1b11cd0
```

3. **Environment Variables**
```bash
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set CLOUDINARY_URL="cloudinary://your-cloudinary-url"
heroku config:set DEBUG=False
```

4. **Deploy Application**
```bash
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### ⚙️ **Configuration Files**

**Procfile:**
```
release: python manage.py collectstatic --noinput
web: gunicorn config.wsgi:application --log-file -
```

**runtime.txt:**
```
python-3.12.8
```

**requirements.txt:**
```
Django==4.2.16
gunicorn==21.2.0
whitenoise==6.8.2
django-allauth==0.57.2
django-crispy-forms==2.3
crispy-bootstrap5==2024.2
django-widget-tweaks==1.5.0
cloudinary==1.41.0
django-cloudinary-storage==0.3.0
dj-database-url==2.2.0
psycopg2==2.9.10
Pillow==10.4.0
```

---

## Credits and Acknowledgements

### 📚 **Educational Resources**
- **Code Institute**: Full Stack Software Development course materials and mentorship
- **Django Documentation**: Official framework documentation and best practices
- **Bootstrap Documentation**: Component usage and responsive design patterns
- **Heroku Dev Center**: Deployment guides and configuration help

### 🛠️ **Technical Resources**
- **GitHub Copilot**: AI-powered development assistance
- **MDN Web Docs**: HTML, CSS, and JavaScript reference materials
- **Cloudinary Documentation**: Image storage and optimization guidance

### 🎨 **Design and Content**
- **Bootstrap**: CSS framework for responsive design
- **FontAwesome**: Icon library for UI elements
- **Unsplash**: Food photography inspiration
- **Google Fonts**: Typography research and selection

### 🙏 **Special Thanks**
- **Code Institute Mentors**: Project guidance and code review
- **GitHub Community**: Open source libraries and contributions
- **Django Community**: Framework development and maintenance
- **Testing Community**: Family and friends who provided user feedback

### 📄 **Third-Party Libraries**
- **Django** (BSD License) - Web framework
- **Bootstrap** (MIT License) - CSS framework
- **FontAwesome** (CC BY 4.0 License) - Icons
- **Cloudinary** - Image storage and optimization

---

*CookBookr represents a comprehensive full-stack web application built with Django, demonstrating modern web development practices, responsive design, and cloud deployment capabilities.*

## Accessibility & WCAG Compliance

Accessibility is a core part of CookBookr's design and development:
- All pages use semantic HTML5 elements (header, nav, main, section, article, aside, footer) for clear structure.
- Interactive elements (buttons, links, forms) include ARIA labels and roles where needed.
- Color contrast and font sizes were checked using WCAG 2.1 AA tools to ensure readability for all users.
- Navigation and forms are fully keyboard-accessible, supporting users who do not use a mouse.
- Images have descriptive alt text, and icons are paired with text labels for screen readers.
- Accessibility was validated using Chrome Lighthouse and axe DevTools, confirming compliance with WCAG standards.

## Real-Time Notifications

Real-time notifications are not currently implemented. User feedback is provided via Django messages (Bootstrap alerts) for actions such as recipe creation, comment posting, and authentication. Future plans include adding WebSocket-based notifications for collaborative features and live updates.

## Automated Testing & Coverage

Automated testing is performed using Django's test framework:
- Unit tests cover models, views, and forms for core features (recipe CRUD, authentication, meal planning).
- Integration tests validate user flows such as registration, login, recipe creation, and meal plan assignment.
- Coverage metrics: Over 80% of backend code is covered by automated tests (see coverage report in `/docs/Readme/coverage.png`).
- Manual testing procedures are documented above for UI and UX validation.

### Copilot-Generated Tests & Reflection

GitHub Copilot was used to generate initial Django unit tests for models and views. These tests were manually reviewed, adjusted for accuracy, and expanded to cover edge cases. Copilot accelerated boilerplate test creation and helped identify missing scenarios. Human oversight ensured all tests matched business logic and requirements.

Copilot's role in test creation:
- Generated test skeletons for models, forms, and views
- Suggested assertions and test data for common cases
- Helped maintain consistent test structure and naming
- Enabled rapid iteration and increased test coverage

All Copilot-generated tests were reviewed and refined for reliability and relevance to project goals.

## Lighthouse Audit Results

CookBookr was tested using Google Lighthouse across multiple key pages (homepage, add recipe, all recipes):

- **Performance:** 98-100
- **Accessibility:** 93-94
- **Best Practices:** 96
- **SEO:** 100

**Highlights:**
- Pages load quickly with minimal blocking time and excellent speed index.
- Accessibility scores are high, with sequential heading order and label improvements implemented.
- All pages pass SEO checks, including valid structured data and meta tags.
- Best practices are followed for security, XSS protection, and HTTPS.

**Continuous Improvement:**
- Minor accessibility warnings (e.g., color contrast, heading order) are actively addressed in templates.
- Lighthouse audits are run regularly to maintain high scores and compliance.