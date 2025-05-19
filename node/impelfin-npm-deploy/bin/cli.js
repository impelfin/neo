#!/usr/bin/env node

const { program } = require('commander');

program.action(cmd => console.log('✓ Running!!'));

program.parse(process.argv);