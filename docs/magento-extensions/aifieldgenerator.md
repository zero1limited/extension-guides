---
title: "API Guidelines"
labels: ["docs", "engineering"]
xxxparent_id: "123456789"           # overrides default CONFLUENCE_PARENT_ID
# xxxconfluence_page_id: "987654321"  # lock to a specific page for updates
---

# AI Field Generators

An AI Field Generator is a tool that automatically fills in fields on your website or system using artificial intelligence.

Instead of a person typing things out manually (like product descriptions, titles, or attributes), the AI can generate them for you — quickly and consistently.

For example:
- If you add a new product, the AI can instantly suggest a title, description, and keywords.
- If you have lots of forms or attributes to fill in (like colour, material, size), the AI can complete them based on patterns it’s learned.
- It saves time, reduces human error, and keeps everything more consistent.

## Prerequisites

Before you install this module please ensure you have a paid Chat GPT account in order to generate API keys.


## Installation

Purchase the extension from https://extensions.zero1.co.uk/ai-field-generator.html

Follow the standard [Magento extension installation guide for Composer](https://docs.zero1.co.uk/magento-extensions/) 
```php
composer require zero1/aifieldgenerator
```

## Configuration

In admin, go to:

- Catolog
- Zero-1 field generator
- Configuration

In general, Enable AI content generation

 Then go to OpenAI API Configuration  and add you Chat GPT API key

[Log into your chat GPT account and click on API keys](https://platform.openai.com/settings/organization/api-keys) 


## Creating Directives

It's key to understand when using AI to generate content, it's important you feed it with good content otherwise you fall victim to the 'shit in - shit out' scenario. A couple of tips

 - Try and make your directive reference far more comprehensive product data (such as description) when attempting to write content. As an example, your AI will serve you better when editing, abbreviating or summarising, than it will elaborating or making more content.

Example
Attribute to Populate: meta_description
Directive `Wria compelling Meta description in less than 40 words using the following information and in a way that would entice the customer to purchase but refrain from starting your response with 'Upgrade your' and trying to ensure that there are very varied responses when we ask you to provide a response. {{product.name}} {{product.description}}`
   
