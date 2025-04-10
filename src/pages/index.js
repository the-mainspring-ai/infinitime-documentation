import clsx from "clsx";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import HomepageFeatures from "@site/src/components/HomepageFeatures";

import Heading from "@theme/Heading";
import styles from "./index.module.css";

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={clsx("hero hero--primary", styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <p className={styles.heroDescription}>
          Welcome to the official documentation hub for InfiniTime - your
          comprehensive resource for time tracking and management solutions.
        </p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro"
            style={{ margin: "0 10px", fontWeight: "bold" }}
          >
            Get Started →
          </Link>
          <Link
            className="button button--outline button--lg"
            to="https://version9.infinitimeonline.net/InfiniTime/winLoginWindow.aspx"
            style={{ margin: "0 10px" }}
          >
            Launch InfiniTime App
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title} - Official Documentation`}
      description="Official documentation for InfiniTime - time tracking and management solutions"
    >
      <HomepageHeader />
      <main>
        <HomepageFeatures />
        <div className="container margin-vert--xl">
          <div className="row">
            <div className="col col--8 col--offset-2 text--center">
              <Heading as="h2">Ready to optimize your time management?</Heading>
              <p>
                Explore our documentation to learn how to make the most of
                InfiniTime's powerful features and capabilities.
              </p>
              <div className={styles.ctaButtons}>
                <Link
                  className="button button--primary button--lg"
                  to="/docs/intro"
                >
                  Read Documentation
                </Link>
              </div>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}
