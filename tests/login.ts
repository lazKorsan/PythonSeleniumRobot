import { Given, When, Then, DataTable } from '@badeball/cypress-cucumber-preprocessor';

Given(`the user is on the login page`, () => {
    // [Given] Sets up the initial state of the system.
});

When(`the user enters {string} and {string}`, (arg0: string, arg1: string) => {
    // [When] Describes the action or event that triggers the scenario.
});

Then(`the user name {string} should be visible`, (arg0: string) => {
    // [Then] Describes the expected outcome or result of the scenario.
});