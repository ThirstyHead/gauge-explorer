/* globals gauge*/
"use strict";
const path = require('path');
const {
    openBrowser,
    closeBrowser,
    goto,
    currentURL,
    client
} = require('taiko');
const assert = require("assert");
const fs = require('fs');
const lighthouse = require('lighthouse/core/index.cjs');
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
});

step("Lighthouse report <filename>", async (filename) => {
    let reportDir = "./reports/lighthouse";
    let url = await currentURL();
    const port = await client()
                       .webSocketUrl.split('/devtools/')[0]
                       .replace('ws://', '')
                       .split(':')[1];
    const options = {output: ['html', 'json', 'csv'], onlyCategories: ['accessibility'], port, logLevel:'error'};
    let runnerResult = await lighthouse(url, options);
    fs.mkdirSync(`${reportDir}`, { recursive: true });
    fs.writeFileSync(`${reportDir}/${filename}.html`, runnerResult.report[0]);
    fs.writeFileSync(`${reportDir}/${filename}.json`, runnerResult.report[1]);
    fs.writeFileSync(`${reportDir}/${filename}.csv`, runnerResult.report[2]);
    console.log('Report(s) written for', runnerResult.lhr.mainDocumentUrl);
    console.log('Accessibility score was', runnerResult.lhr.categories.accessibility.score * 100);
});

