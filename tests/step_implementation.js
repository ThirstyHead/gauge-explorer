/* globals gauge*/
"use strict";
const path = require('path');
const {
    openBrowser,
    closeBrowser,
    goto
} = require('taiko');
const assert = require("assert");
const headless = process.env.headless_chrome.toLowerCase() === 'true';

step("Open browser", async () => {
    await openBrowser();
});

step("Close browser", async () => {
    await closeBrowser();
});

step("Visit <url>", async (url) => {
    try{
        await goto(url, {timeout:60000});
    } catch(e){ 
        console.log(e.message);
    }
});

step("Message <msg>", async (msg) => {
    console.log(msg);
})
