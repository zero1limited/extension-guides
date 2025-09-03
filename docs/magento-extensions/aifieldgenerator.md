# AI Field Generators

nbnhfnfnhfhnf 
Experience seamless compliance with the upcoming PCI DSS requirements with ZERO-1's PCI Admin User Requirements, a Magento 2 extension designed to simplify the process for merchants.



## Installation
Purchase the extension from https://extensions.zero1.co.uk/ai-field-generator.html

Follow the standard [Magento extension installation guide for Composer](https://docs.zero1.co.uk/magento-extensions/) 
```php
composer require zero1/aifieldgenerator
```


## Configuration

It's key to understand when using AI to generate content, it's important you feed it with good content otherwise you fall victim to the 'shit in - shit out' scenario. A couple of tips

 - Try and make your directive reference far more comprehensive product data (such as description) when attempting to write content. As an example, your AI will serve you better when editing, abbreviating or summarising, than it will elaborating or making more content.

Example
Attribute to Populate: meta_description
Directive `Wria compelling Meta description in less than 40 words using the following information and in a way that would entice the customer to purchase but refrain from starting your response with 'Upgrade your' and trying to ensure that there are very varied responses when we ask you to provide a response. {{product.name}} {{product.description}}`
   
