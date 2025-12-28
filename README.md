# ምስል (Misel) Art Market - SCM Project

## Project Overview
This is a Software Configuration Management (SCM) mini-project. It demonstrates the application of SCM principles, including configuration identification, baseline management, and change control using a Django-based Art Gallery system.

## Repository Structure
- **/docs**: Contains SCMP, Requirements, and Audit Reports.
- **/src**: The Django source code, templates, and application logic.
- **/tests**: Audit checklists and functional test records.
- **db.sqlite3**: The baselined database schema.
- **manage.py**: Project management script.

## SCM Milestones (Tags)
This repository uses the following tags to mark baselines:
- `BL1`: Initial repository setup and documentation.
- `BL2`: Functional core (Authentication system).
- `BL3`: Feature complete (File upload & Gallery management).
- `BL-FINAL`: Final audited system with premium UI.

## Local Setup Instructions
1. **Clone the repository:**
   `git clone [Your-Repository-URL]`

2. **Install Dependencies:**
   `pip install django pillow`

3. **Initialize Database:**
   `python manage.py migrate`

4. **Run the System:**
   `python manage.py runserver`
   Access via: http://127.0.0.1:8000/

## Change Control
All modifications follow the Change Request (CR) process defined in the SCMP. Refer to `/docs/SCMP_Plan.pdf` for the full change management workflow.