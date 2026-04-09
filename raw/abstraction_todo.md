Journal
- configuration file for settings
    - JOURNAL_FOLDER, FILE_PREFIX, FILE_EXTENSION
    - Settings reader, plops user's markdown into config object
    - questions morning and questions night
- helper functions file that are generic
    - format_date
    - what time of day is it
    - given time of day, what greetings appropriate
- FileHandler should be generic read/write input into file given config
    - get_append_or_create mode method
- Template files + variable names
- Entry create method should use FileHandler
- JournalEntry could inherit a
    Document (which handles generic things, date setter, template, creations with FileHandler)
    JournalEntry would change template write data returned from Prompt
- JournalPrompt
    - PromtSession (promt types: freeform, Q&A-freeform, Q&A-integer, etc., )
        - intro, input session, outro

Quotes
- a quote could be a Document + template + data from api
- api data getter (request url, keys to get from response, handle errors, return some data to write to template)