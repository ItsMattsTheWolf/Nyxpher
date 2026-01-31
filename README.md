# Description

Nyxpher is a personal text encryption/decryption tool based on the Nyx27 cipher. It is the official runner and reference implementation of Nyx27, both designed and developed by ItsMattsTheWolf.

# Overview
Nyxpher is a personal application designed to encrypt and decrypt text using the Nyx27 cipher.
It is not a security system and does not aim to protect sensitive data; its purpose is to hide text in a reversible way using its own rules.

# About Nyxpher

What is it?

  Nyxpher is a console-based tool that allows users to apply the Nyx27 cipher to any text they provide.
  It is the official runner and the main reference implementation of the Nyx27 cipher.

How is it used?

  The user first chooses whether to encrypt or decrypt a message.
  Then, the text is entered, and Nyxpher automatically applies the Nyx27 cipher rules to produce the result.

  The process is straightforward, with no additional configuration or intermediate steps.

What can it be used for?

  - Manually hiding messages.
  - Exchanging encrypted texts between people.
  - Personal, recreational, or creative use.
  - Projects where real security is not required.

  Nyxpher is not cryptography, and it does not replace systems used by banks, databases, or messaging applications.

  Note: Do not attempt to use it for those purposes. Encryption systems used by banks and applications are completely different.
  Implementing Nyx27 in such contexts will not work and will make your application less secure.

# About Nyx27

What is it?

  Nyx27 is a custom substitution cipher that uses a 27-letter alphabet, designed to allow consistent and reversible text encryption and decryption.

Original idea

  The original idea behind Nyx27 is to create a simple system for hiding text, based on a symmetrical alphabet structure and clear rules, without relying on cryptographic standards or unnecessary complexity.

How does it work?

  The alphabet is divided into three parts:

  - An initial block of 13 letters

  - A central letter that acts as an axis

  - A final block of 13 letters

  Each letter is transformed using a shift and mirror system around the central axis.
  The same logic allows the process to be reversed, making it possible to decrypt previously encrypted text without information loss.

  The rules are deterministic: the same input text will always produce the same output under Nyx27.

# Author
Nyxpher and the Nyx27 cipher were created by ItsMattsTheWolf.
