# HQL

A SQL inspired query language for HTML documents.

## Goals

I have two goals for this project:

1. Learn/practice Python
I am just now learning Python and wanted a project to do with it.  I figured this might be a good one since it has the opportunity for data analysis.

1. Create a new language for fun
I thought it'd be an interesting experiment to create a new language.


These two things being the main reasonings, I'm expecting some big diffs, big re-writes, and probably a few start overs.  We'll see how this goes.


# Installation

I honestly do not know how you are supposed to install this package... Supposedly the below will do it, but I'm not so sure...

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

```bash
$ pipsi install .
```

# Usage

## Starting up

```bash
$ hql https://www.python.org
```

Start up the app by running `hql`.  You also may add an optional URL to connect and request an html file in one go.

## Operations

There are several commands you can run once inside the HQL environment.

- exit - to exit the environment
- help - to see the help menu (it looks a lot like this list)
- refresh - to re-query the currently set url
- response - to see the HTML response
- url - to retrieve and set the current url

### URL Command

The `url` command can be use two ways.  Just typing it alone will print the currently set url:

```
url
```

It also takes an optional second argument that can be used to set the url.

```
url https://pypi.python.org/pypi
```

## Querying

Querying is currently set up to mimic SQL queries, but please know that it is no where near as feature-filled at the moment.
The four query sections accepted are (in order):

- SELECT: (required) followed by the properties and attributes that you'd like to select from the returned html
- WHERE: followed by the selection criteria for the query.
- LIMIT: max number of responses
- OFFSET: how many responses to skip in the beginning

### Select

You can select any number of values, but currently you cannot send a `*` to get them all (yet).

```sql
SELECT name class id
```

### Where

Currently, the where clause only accepts one equality match.

```sql
SELECT name WHERE class = btn
```

### Limit and Offset

Both accept one number.  They can be used in conjunction or separately.

```sql
SELECT name LIMIT 10 OFFSET 5
```

## Selections

Currently you can query and select these properties of the HTML element
- attributes (like `class`, `id`, `href`, etc.  except `name` for now)
- children
- name (the tag name like `div`)
- parent
- text
