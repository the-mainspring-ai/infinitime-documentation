// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import { themes as prismThemes } from "prism-react-renderer";

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Introduction",
  tagline: "Documentation for the InfiniTime Online Project",
  favicon: "favicon.ico",

  // Set the production url of your site here
  url: "https://infinitimeonline.net",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/",
  deploymentBranch: "gh-pages",
  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "the-mainspring-ai", // Usually your GitHub org/user name.
  projectName: "infinitime-documentation", // Usually your repo name.

  onBrokenLinks: "warn",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: "./sidebars.js",
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl: "https://github.com/InfiniTimeOrg/infintime-docs/tree/main/",
        },

        theme: {
          customCss: "./src/css/custom.css",
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: "img/docusaurus-social-card.jpg",
      navbar: {
        title: "InfiniTime Documentation",
        logo: {
          alt: "InfiniTime Logo",
          src: "infinitime-logo.png",
        },
        items: [
          {
            to: "https://version9.infinitimeonline.net/InfiniTime/winLoginWindow.aspx",
            label: "Infinitime App",
            position: "right",
          },
          {
            href: "https://github.com/InfiniTimeOrg/infintime-docs",
            label: "GitHub",
            position: "right",
          },
        ],
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "Docs",
            items: [
              {
                label: "Documentation",
                to: "/docs/intro",
              },
            ],
          },

          {
            title: "More",
            items: [
              {
                label: "GitHub",
                href: "https://github.com/InfiniTimeOrg/infintime-docs",
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} InfiniTime Project. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
