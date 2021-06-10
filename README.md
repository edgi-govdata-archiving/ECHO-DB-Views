# ECHO-DB-Views
Scripts for setting up and testing views for the ECHO database.
Create Views in the database to better prepare the data for use in the Jupyter notebooks.

Use data in FL5_CSVs to test the setup and use of views with sqlite. The FL5-CVs .csv
files are adequate to test the process that might be used in the Stonybrook database:
 - edgi_echo.py - A script that builds an EXP_PGM table for linking indexes between 
  ECHO_EXPORTER and the numerous program tables.
 - create_views.sql - The SQL commands to build the database Views.
 
 For simplicity this is done using Sqlite.  It should be easy to translate this to MySQL.

1.  sqlite3 edgi_echo.db
2.  Import data:
    sqlite> .mode csv
    sqlite> .import FL5_CSVs/ECHO_EXPORTER-FL-CongressionalDistrict-5.csv ECHO_EXPORTER
    sqlite> .import FL5_CSVs/RCRA_Violations.csv RCRA_VIOLATIONS
    sqlite> .import FL5_CSVs/RCRA_Inspections.csv RCRA_EVALUATIONS
    sqlite> .import FL5_CSVs/RCRA_Enforcements.csv RCRA_ENFORCEMENTS
    sqlite> .import FL5_CSVs/Air_Inspections.csv ICIS_FEC_EPA_INSPECTIONS
    sqlite> .import FL5_CSVs/Air_Violations.csv ICIS_AIR_VIOLATION_HISTORY
    sqlite> .import FL5_CSVs/Air_Formal_Actions.csv ICIS_AIR_FORMAL_ACTIONS
    sqlite> .import FL5_CSVs/Air_Compliance.csv ICIS_AIR_FCES_PCES
    sqlite> .import FL5_CSVs/Combined_Air_Emissions.csv POLL_RPT_COMBINED_EMISSIONS
    sqlite> .import FL5_CSVs/Water_Quarterly_Violations.csv NPDES_QNCR_HISTORY
    sqlite> .import FL5_CSVs/Clean_Water_Inspections.csv NPDES_INSPECTIONS
    sqlite> .import FL5_CSVs/Clean_Water_Enforcements.csv NPDES_FORMAL_ENFORCEMENT_ACTIONS
    sqlite> .import FL5_CSVs/SDWA_Site_Visits.csv SDWA_SITE_VISITS
    sqlite> .import FL5_CSVs/SDWA_Enforcements.csv SDWA_ENFORCEMENTS
    sqlite> .import FL5_CSVs/SDWA_Public_Water_Systems.csv SDWA_PUB_WATER_SYSTEMS
    sqlite> .import FL5_CSVs/SDWA_Violations.csv SDWA_VIOLATIONS
    sqlite> .import FL5_CSVs/SDWA_Serious_Violators.csv SDWA_SERIOUS_VIOLATORS
    (These have been edited so that the header field 'Index' is changed to the
    table's appropriate index field--see make_data_sets.py or create_views.sql.)
3.  Create the EXP_PGM linking table and the Views:
    sqlite> .read create_views.sql
    (The create_views.sql should only be checked into Github with the MySQL version
    of those tables with '-' characters in their names.)
4.  Check a few of the views to see that they have records.
    sqlite> select count(*) from RCRA_ENFORCEMENTS_VIEW;
    1601
    sqlite> select count(*) from ICIS_AIR_VIOLATION_HISTORY;
    86
