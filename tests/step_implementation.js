/* globals gauge*/
"use strict";
//import lighthouse from 'lighthouse';
// const lighthouse = require('lighthouse');

const path = require('path');
const {
    openBrowser,
    closeBrowser,
    goto
} = require('taiko');
const assert = require("assert");
const fs = require('fs');
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

// step("Lighthouse report <filename>", async (filename) => {
//     let url = await currentURL();
//     const port = await client()
//                        .webSocketUrl.split('/devtools/')[0]
//                        .replace('ws://', '')
//                        .split(':')[1];
//     const options = {output: 'html', onlyCategories: ['accessibility'], port, logLevel:'error'};
//     let runnerResult = await lighthouse(url, options);
//     fs.writeFileSync(`${filename}.html`, runnerResult.report);
//     console.log('Report written for', runnerResult.lhr.finalUrl);
//     console.log('Accessibility score was', runnerResult.lhr.categories.accessibility.score * 100);
// });

